from enum import StrEnum


class RoguelikeGameItemSubType(StrEnum):
    NONE = "NONE"
    CURSE = "CURSE"
    TEMP_TICKET = "TEMP_TICKET"
    TOTEM_UPPER = "TOTEM_UPPER"
    TOTEM_LOWER = "TOTEM_LOWER"
    SECRET = "SECRET"
    SINGLE_RAND_FREE = "SINGLE_RAND_FREE"
    RED_CAPSULE = "RED_CAPSULE"
