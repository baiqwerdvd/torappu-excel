from enum import StrEnum


class AutoChessBroadcastType(StrEnum):
    NONE = "NONE"
    GOLDEN_CHAR = "GOLDEN_CHAR"
    SHOP_LEVEL = "SHOP_LEVEL"
    BOSS_HIT = "BOSS_HIT"
    CHAR_DAMAGE = "CHAR_DAMAGE"
    CHAR_GIFT = "CHAR_GIFT"
    BOND_EFFECT = "BOND_EFFECT"
