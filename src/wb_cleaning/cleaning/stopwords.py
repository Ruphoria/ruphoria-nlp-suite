"""This module contains the central stopwords list for the wb_cleaning library.
"""
from nltk.corpus import stopwords as nltk_stopwords

roman_nums = set([
    "i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x", "xi", "xii", "xiii", "xiv", "xv",
    "xvi", "xvii", "xviii", "xix", "xx", "xxi", "xxii", "xxiii", "xxiv", "xxv", "xxvi", "xxvii",
    "xxviii", "xxix", "xxx", "xxxi", "xxxii", "xxxiii", "xxxiv", "xxxv", "xxxvi", "xxxvii",
    "xxxviii", "xxxix", "xl", "xli", "xlii", "xliii", "xliv", "xlv", "xlvi", "xlvii", "xlviii",
    "xlix", "l", "li", "lii", "liii", "liv", "lv", "lvi", "lvii", "lviii", "lix", "lx", "lxi",
    "lxii", "lxiii", "lxiv", "lxv", "lxvi", "lxvii", "lxviii", "lxix", "lxx", "lxxi", "lxxii",
    "lxxiii", "lxxiv", "lxxv", "lxxvi", "lxxvii", "lxxviii", "lxxix", "lxxx", "lxxxi",
    "lxxxii", "lxxxiii", "lxxxiv", "lxxxv", "lxxxvi", "lxxxvii", "lxxxviii", "lxxxix", "xc", "xci",
    "xcii", "xciii", "xciv", "xcv", "xcvi", "xcvii", "xcviii", "xcix", "c",
])

noise_words = set([
    "ovid",
    "include", "shall", "tion", "ment", "provide",
    "cator",
    "typically", "usually", "evidently", "invariably", "oftentimes", "surprisingly", "presumably",
    "generally", "especially", "likely", "apparently", "essentially", "largely", "notably", "consequently",
    "finally", "furthermore", "somewhat", "fairly", "likewise", "importantly", "additionally", "specifically",
    "typically", "addition",
    "instance", "similarly", "lastly",
])

# https://www.ranks.nl/stopwords
mysql_stops = [
    "a's",
    "able",
    "about",
    "above",
    "according",
    "accordingly",
    "across",
    "actually",
    "after",
    "afterwards",
    "again",
    "against",
    "ain't",
    "all",
    "allow",
    "allows",
    "almost",
    "alone",
    "along",
    "already",
    "also",
    "although",
    "always",
    "am",
    "among",
    "amongst",
    "an",
    "and",
    "another",
    "any",
    "anybody",
    "anyhow",
    "anyone",
    "anything",
    "anyway",
    "anyways",
    "anywhere",
    "apart",
    "appear",
    "appreciate",
    "appropriate",
    "are",
    "aren't",
    "around",
    "as",
    "aside",
    "ask",
    "asking",
    "associated",
    "at",
    "available",
    "away",
    "awfully",
    "be",
    "became",
    "because",
    "become",
    "becomes",
    "becoming",
    "been",
    "before",
    "beforehand",
    "behind",
    "being",
    "believe",
    "below",
    "beside",
    "besides",
    "best",
    "better",
    "between",
    "beyond",
    "both",
    "brief",
    "but",
    "by",
    "c'mon",
    "c's",
    "came",
    "can",
    "can't",
    "cannot",
    "cant",
    "cause",
    "causes",
    "certain",
    "certainly",
    "changes",
    "clearly",
    "co",
    "com",
    "come",
    "comes",
    "concerning",
    "consequently",
    "consider",
    "considering",
    "contain",
    "containing",
    "contains",
    "corresponding",
    "could",
    "couldn't",
    "course",
    "currently",
    "definitely",
    "described",
    "despite",
    "did",
    "didn't",
    "different",
    "do",
    "does",
    "doesn't",
    "doing",
    "don't",
    "done",
    "down",
    "downwards",
    "during",
    "each",
    "edu",
    "eg",
    # "eight",
    "either",
    "else",
    "elsewhere",
    "enough",
    "entirely",
    "especially",
    "et",
    "etc",
    "even",
    "ever",
    "every",
    "everybody",
    "everyone",
    "everything",
    "everywhere",
    "ex",
    "exactly",
    "example",
    "except",
    "far",
    "few",
    "fifth",
    "first",
    # "five",
    "followed",
    "following",
    "follows",
    "for",
    "former",
    "formerly",
    "forth",
    # "four",
    "from",
    "further",
    "furthermore",
    "get",
    "gets",
    "getting",
    "given",
    "gives",
    "go",
    "goes",
    "going",
    "gone",
    "got",
    "gotten",
    "greetings",
    "had",
    "hadn't",
    "happens",
    "hardly",
    "has",
    "hasn't",
    "have",
    "haven't",
    "having",
    "he",
    "he's",
    "hello",
    "help",
    "hence",
    "her",
    "here",
    "here's",
    "hereafter",
    "hereby",
    "herein",
    "hereupon",
    "hers",
    "herself",
    "hi",
    "him",
    "himself",
    "his",
    "hither",
    "hopefully",
    "how",
    "howbeit",
    "however",
    "i'd",
    "i'll",
    "i'm",
    "i've",
    "ie",
    "if",
    "ignored",
    "immediate",
    "in",
    "inasmuch",
    "inc",
    "indeed",
    "indicate",
    "indicated",
    "indicates",
    "inner",
    "insofar",
    "instead",
    "into",
    "inward",
    "is",
    "isn't",
    "it",
    "it'd",
    "it'll",
    "it's",
 