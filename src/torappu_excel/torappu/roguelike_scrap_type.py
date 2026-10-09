from ..common import CustomIntEnum


class RoguelikeScrapType(CustomIntEnum):
    ERROR = "ERROR", -1
    NONE = "NONE", 0
    MOVE = "MOVE", 1
    GOODS = "GOODS", 2
    PASSIVE = "PASSIVE", 3
