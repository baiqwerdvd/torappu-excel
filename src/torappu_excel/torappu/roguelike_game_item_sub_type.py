from ..common import CustomIntEnum


class RoguelikeGameItemSubType(CustomIntEnum):
    NONE = "NONE", 0
    CURSE = "CURSE", 1
    TEMP_TICKET = "TEMP_TICKET", 2
    TOTEM_UPPER = "TOTEM_UPPER", 4
    TOTEM_LOWER = "TOTEM_LOWER", 8
    SECRET = "SECRET", 16
    SINGLE_RAND_FREE = "SINGLE_RAND_FREE", 32
