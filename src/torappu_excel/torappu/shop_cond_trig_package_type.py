from enum import StrEnum


class ShopCondTrigPackageType(StrEnum):
    NONE = "NONE"
    RETURN_PROGRESS = "RETURN_PROGRESS"
    RETURN_ONCE = "RETURN_ONCE"
    NEW_PROGRESS = "NEW_PROGRESS"
