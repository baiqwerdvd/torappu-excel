from enum import IntEnum

from ..common import CustomIntEnum


class SandboxV2WeatherType(CustomIntEnum):
    NORMAL = "NORMAL", 0
    RAINFOREST = "RAINFOREST", 1
    VOLCANO = "VOLCANO", 2
    DESERT = "DESERT", 3


class SandboxV2WeatherTypeEnum(IntEnum):
    NORMAL = 0
    RAINFOREST = 1
    VOLCANO = 2
    DESERT = 3
