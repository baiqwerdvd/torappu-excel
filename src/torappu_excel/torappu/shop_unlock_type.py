from enum import StrEnum


class ShopUnlockType(StrEnum):
    ALWAYS_UNLOCK = "ALWAYS_UNLOCK"
    SKIN_UNLOCK = "SKIN_UNLOCK"
    FURN_UNLOCK = "FURN_UNLOCK"
    BOTH_SKIN_FURN = "BOTH_SKIN_FURN"
