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
    latin_america_and_caribbean = "Latin America and Caribbean"
    middle_east_and_north_africa = "Middle East and North Africa"
    # oth = "OTH"
    # other = "Other"
    others = "Others"
    rest_of_the_world = "Rest Of The World"
    south_asia = "South Asia"
    the_world_region = "The World Region"

    @classmethod
    def clean(cls, value):

        mappings = {
            "latin america & caribbean": "Latin America and Caribbean",
            "latin america &amp; caribbean": "Latin America and Caribbean",
            "oth": "Others",
            "other": "Others",
            None: "",
        }

        value = mappings.get(value.lower(), value)

        return value


class WBDocTypes(WBEnum):
    '''Curated list of document types.

    delimiter = ","

    TODO: For further review

    {'': 15819,
    'Financial Sector Assessment Program (FSAP)': 146,
    'Auditing Document,Financial Monitoring Report,Memorandum,Letter': 138,
    'IEG Approach Paper': 122,
    'Investment Climate Assessment (ICA)': 103,
    'Economic Updates and Modeling': 103,
    'Energy Study': 102,
    'Other Education Study': 83,
    'Inspection Panel Notice of Registration': 79,
    'General Economy, Macroeconomics and Growth Study': 78,
    'Safeguards Diagnostic Review': 72,
    'Interim Strategy Note': 71,
    'World Development Indicators': 65,
    'Country Financial Accountability Assessment': 64,
    'Corporate Governance Assessment (ROSC)': 63,
    'Social Analysis': 62,
    'Other Rural Study': 59,
    'Foreign Trade, FDI, and Capital Flows Study': 58,
    'Country Procurement Assessment (CPAR)': 56,
    'Other Urban Study': 56,
    'GEF Project Brief': 55,
    'Development Policy Review (DPR)': 52,
    'Country Environmental Analysis (CEA)': 52,
    'Integrative Fiduciary Assessment': 52,
    'Education Sector Review': 49,
    'Manual': 47,
    'Investigation Report': 45,
    'Health Sector Review': 42,
    'Sector or Thematic Evaluation': 42,
    'Tranche Release Document': 41,
    'Country Assistance Evaluation': 40,
    'Commodity Working Paper': 40,
    'Program-for-Results Fiduciary Systems Assessment': 39,
    'PSD, Privatization and Industrial Policy': 38,
    'Program-for-Results Technical Assessment': 38,
    'Mining/Oil and Gas': 33,
    'Water & Sanitation Discussion Paper': 31,
    'Country Partnership Framework': 31,
    'Knowledge Economy Study': 29,
    'Global Development Finance - formerly World Debt Tables': 28,
    'Other Financial Accountability Study': 28,
    'City Development Strategy (CDS)': 27,
    'Institutional and Governance Review (IGR)': 27,
    'Country Gender Assessment (CGA)': 26,
    'Internal Discussion Paper': 26,
    'Environment Working Paper': 23,
    'Memorandum & Recommendation of the Director': 22,
    'Global Environment Facility Working Paper': 20,
    'Corporate Evaluation': 19,

    'Women in Development and Gender Study': 19,
    'Rural Development Assessment': 19,
    'Risk and Vulnerability Assessment': 17,
    "Governor's Statement": 17,
    'Memorandum,Financial Monitoring Report,Letter,Auditing Document': 16,
    'LAC Human & Social Development Group Paper Series': 16,
    'Memorandum & Recommendation of the Managing Director': 16,
    'Project Appraisal Document Data Sheet': 15,
    'Strategic Environmental Assessment/Analysis': 14,
    'Legal and Judicial Sector Assessment': 13,
    'Energy-Environment Review': 13,
    'Policy Paper': 13,
    'Country Portfolio Performance Review': 13,
    'Law and Justice Study': 13,
    'Impact Evaluation Report': 13,
    'Country Infrastructure Framework': 12,
    'Report on the World Bank Research Program': 12,
    'Country Engagement Note': 12,
    'Completion Point Document': 11,
    'Other Procurement Study': 10,
    'Commodities Study': 10,
    'GEF Project Document': 10,
    'Preliminary Decision Point Document': 9,
    'Insolvency Assessment (ROSC)': 9,
    'Annual Report on Portfolio Performance': 7,
    'Public Investment Review': 7,
    'Deliverable Document': 7,
    'Transitional Support Strategy': 6,
    'Memorandum &amp; Recommendation of the President': 6,
    'Directory': 5,
    'Country Re-engagement Note': 5,
    'Environmental and Social Framework': 5,
    'Financial Flows': 4,
    'World Bank Atlas': 4,
    'Debt and Creditworthiness Study': 4,
    'Financial Assessment': 4,
    'Price Prospects for Major Primary Commodities': 4,
    'Legal Opinion': 3,
    'Environmental Action Plan': 3,
    'Memorandum,Agreement': 3,
    'Human Capital Working Paper': 3,
    'President&apos;s Report': 3,
    'Decision Point Document': 2,
    'CAS Public Information Note': 2,
    'Project Concept Note': 2,
    'P4R-AF-DRFT-ESSA': 2,
    'Social Action Plan': 2,
    'Environmental Action Plan,Social Action Plan': 2,
    "Managing Director's Report": 2,
    'Public Environmental Expenditure Review (PEER)': 1,
    'Poverty & Social Policy Working Paper': 1,
    'Economic Report': 1,
    'Memorandum,Financial Monitoring Report,Auditing Document,Le