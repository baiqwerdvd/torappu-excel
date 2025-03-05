from ..common import CustomIntEnum


class UniEquipTarget(CustomIntEnum):
    NONE = "NONE", 0
    TRAIT = "TRAIT", 1
    TRAIT_DATA_ONLY = "TRAIT_DATA_ONLY", 2
    TALENT = "TALENT", 3
    TALENT_DATA_ONLY = "TALENT_DATA_ONLY", 4
    DISPLAY = "DISPLAY", 5
    OVERWRITE_BATTLE_DATA = "OVERWRITE_BATTLE_DATA", 6
