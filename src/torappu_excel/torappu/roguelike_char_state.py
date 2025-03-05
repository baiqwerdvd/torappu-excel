from enum import StrEnum


class RoguelikeCharState(StrEnum):
    NORMAL = "NORMAL"
    UPGRADE = "UPGRADE"
    UPGRADE_BUFF = "UPGRADE_BUFF"
    UPGRADE_BONUS = "UPGRADE_BONUS"
    FREE = "FREE"
    ASSIST = "ASSIST"
    THIRD = "THIRD"
    MONTHLY = "MONTHLY"
    THIRD_LOW = "THIRD_LOW"
