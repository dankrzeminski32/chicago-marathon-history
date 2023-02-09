from enum import Enum


class SEX(Enum):
    """Used to represent genders in our database and application"""

    NOT_KNOWN = 0
    MALE = 1
    FEMALE = 2
    NOT_APPLICABLE = 9


class ENDPOINTS(Enum):
    """Used to represent the url strings for our api endpoints"""

    ATHLETES = "/api/athletes/"
    MARATHONS = "/api/marathons/"
    RESULTS = "/api/results/"


class ERROR_MESSAGES(Enum):
    INVALID_YEAR = "Invalid year, please try again."
    INVALID_SEX_INPUT = "Sex must be either 'M' or 'F'"
