from ..common import CustomIntEnum


class ActMultiV3IdentityType(CustomIntEnum):
    NONE = "NONE", 0
    HIGH = "HIGH", 1
    LOW = "LOW", 2
    TEMPORARY = "TEMPORARY", 3
    ALL = "ALL", 4
