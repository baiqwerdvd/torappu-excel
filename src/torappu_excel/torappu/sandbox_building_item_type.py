from enum import StrEnum


class SandboxBuildingItemType(StrEnum):
    NONE = "NONE"
    PRODUCTION = "PRODUCTION"
    SCOUT = "SCOUT"
    BATTLE = "BATTLE"
    FUNCTION = "FUNCTION"
