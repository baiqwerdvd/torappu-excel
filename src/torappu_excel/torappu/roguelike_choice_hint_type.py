from ..common import CustomIntEnum


class RoguelikeChoiceHintType(CustomIntEnum):
    NONE = "NONE", 0
    ITEM = "ITEM", 1
    SACRIFICE = "SACRIFICE", 2
    SACRIFICE_TOTEM = "SACRIFICE_TOTEM", 3
    EXPEDITION = "EXPEDITION", 4
    VISION = "VISION", 5
    CHAOS = "CHAOS", 6
    FRAGMENT = "FRAGMENT", 7
