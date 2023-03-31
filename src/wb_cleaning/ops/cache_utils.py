# Implement redis cacher
'''This module wraps the redis server to serve primarily as a caching service.

# # If not yet present, instantiate a docker instance of redis using the following command...
# docker run --name=wb-cleaning-redis --publish=6379:6379 --hostname=redis --restart=on-failure --detach redis:latest
# docker stop wb-cleaning-redis
# WB_CLEANING_REDIS_HOSTNAME=localhost python

'''
import os
import json
import joblib
import redis


def get_redis_params():
    '''Extracts redis params from env but fallsback to container host if not present.
    '''

    redis_host = os.environ.get(
        'WB_CLEANING_REDIS_HOSTNAME', 'redis')  # 'localhost')
    redis_port = os.environ.get('WB_CLEANING_REDIS_PORT', '6379')
    redis_db = os.environ.get('WB_CLEANING_REDIS_DB', '0')
    redis_url = f'redis://{redis_host}:{redis_port}/{redis_db}'

    return dict(
        redis_host=redis_host,
        redis_port=redis_port,
        redis_db=redis_db,
        redis_url=redis_url
    )


def get_redis():
    '''Creates a redis instance based on the params set.
    '''
    redis_params = get_redis_params()
    cache = redis.Redis(
        host=redis_params.get('redis_host'),
        port=redis_params.get('redis_port'),
        db=redis_params.get('redis_db'),
    )

    return cache


CACHE_HASH_BUCKET = 'cache-hashes'

try:
    redis_cache = get_redis()
    redis_cache.hset('test', '1029', '1029')
except redis.ConnectionError:
    # Fallback to localhost
    os.environ['WB_CLEANING_REDIS_HOSTNAME'] = 'localhost'
    redis_cache = get_redis()

    try:
        redis_cache.hset('test', '1029', '1029')
    except redis.ConnectionError as er