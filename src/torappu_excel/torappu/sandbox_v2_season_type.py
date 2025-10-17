from enum import IntEnum

from ..common import CustomIntEnum


class SandboxV2SeasonType(CustomIntEnum):
    NONE = "NONE", 0
    DRY = "DRY", 1
    RAINY = "RAINY", 2
    CHALLENGE = "CHALLENGE", 3


class SandboxV2SeasonTypeEnum(IntEnum):
    NONE = 0
    DRY = 1
    RAINY = 2
    CHALLENGE = 3
