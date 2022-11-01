from enum import Enum


class Sex(Enum):
    """Used to represent genders in our database and application"""
    NOT_KNOWN = 0
    MALE = 1
    FEMALE = 2
    NOT_APPLICABLE = 9