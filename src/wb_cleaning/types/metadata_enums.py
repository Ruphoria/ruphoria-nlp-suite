"""This module contains the curated list of values found in the
WB docs API as well as other constants used in the metadata fields.
"""
import abc
import enum
import re
import requests
from bs4 import BeautifulSoup


def get_wb_curated_list(list_id):
    """Enumerates the list of items corresponding to the given `list_id` found in the
    World Bank's wds API.

    Source: https://search.worldbank.org/api/v2/wds

    Example:
        list_id = "geo_reg"
    """
    r = requests.get('https://search.worldbank.org/api/v2/wds')
    b = BeautifulSoup(r.content, 'html.parser')

    item_list = b.find('select', id=list_id).find_all('option')
    g = {re.sub(r'[^a-z]+', '_', o.text.lower()).strip('_'): o.text for o in item_list}

    for k, v in g.items():
        print(f'{k} = "{v}"')


class WBEnum(enum.Enum):

    @classmethod
    @abc.abstractmethod
    def clean(cls, value):
        """This method allows us to perform cleaning of the metadata.
        """
        return

    @classmethod
    def _missing_(cls, value):
        """Use the `clean` method to perform the normalization of input values.
        """
        enum_values = set(e.value for e in cls)

        value = cls.clean(value)

        if value not in enum_values:
            raise ValueError("%r is not a valid %s" % (value, cls.__name__))

        return cls(value)


class Corpus(WBEnum):
    ADB = "ADB"
    AFDB = "AFDB"
    ECLAC = "ECLAC"
    EPDC = "EPDC"
    ESCAP = "ESCAP"
    FAO = "FAO"
    IADB = "IADB"
    IIEP = "IIEP"
    IMF = "IMF"
    OECD = "OECD"
    UNECA = "UNECA"
    UNESCWA = "UNESCWA"
    UNHCR = "UNHCR"
    UNIDO = "UNIDO"
    UNODC = "UNODC"
    UNPD = "UNPD"
    WFP = "WFP"
    WB = "WB"

    @classmethod
    def clean(cls, value):
        value = value.upper()

        mappings = {
            "IDB": "IADB",
        }

        value = mappings.get(value, value)

        return value


class WBGeographicRegions(WBEnum):
    '''Curated list of geographic regions.

    delimiter = "|"

    TODO: For further review

    {'': 130220,
    'Latin America & Caribbean': 3992,
    'East Asia and Pacific': 4320,
    'South Eastern Europe and Balkans': 6332,
    'Middle East and North Africa': 3559}

    '''
    # Manually defined
    EMPTY = ""
    latin_america_and_caribbean = "Latin America and Caribbean"
    east_asia_and_pacific = "East Asia and Pacific"
    south_eastern_europe_and_balkans = "South Eastern Europe and Balkans"
    middle_east_and_north_africa = "Middle East and North Africa"

    # From WB docs API curated list
    africa = "Africa"
    america = "America"
    asia = "Asia"
    caribbean = "Caribbean"
    central_africa = "Central Africa"
    central_america = "Central America"
    central_asia = "Central Asia"
    commonwealth_of_independent_states = "Commonwealth of Independent States"
    east_africa = "East Africa"
    east_asia = "East Asia"
    eastern_europe = "Eastern Europe"
    europe = "Europe"
    europe_and_central_asia = "Europe and Central Asia"
    europe_middle_east_and_north_africa = "Europe, Middle East and North Africa"
    european_union = "European Union"
    latin_america = "Latin America"
    middle_east = "Middle East"
    north_africa = "North Africa"
    north_america = "North America"
    oceania = "Oceania"
    sahel = "Sahel"
    south_america = "South America"
    south_asia = "South Asia"
    southeast_asia = "Southeast Asia"
    southern_africa = "Southern Africa"
    sub_saharan_africa = "Sub-Saharan Africa"
    west_africa = "West Africa"
    world = "World"

    @classmethod
    def clean(cls, value):
        mappings = {
            "latin america & caribbean": "Latin America and Caribbean",
            "africa west": "West Africa",
            None: "",
        }

        value = mappings.get(value.lower(), value)

        return value


class WBAdminRegions(WBEnum):
    '''Curated list of administrative regions.

    delimiter = ","

    TODO: For further review

    {'': 14150, 'OTHER': 1}

    '''
    # Manually defined
    EMPTY = ""

    # From WB docs API curated list
    africa = "Africa"
    africa_east = "Africa East"
    africa_west = "Africa West"
    east_asia_and_pacific = "East Asia and Pacific"
    europe_and_central_asia = "Europe and Central Asia"
    latin_ame