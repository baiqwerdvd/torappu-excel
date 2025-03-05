from ..common import CustomIntEnum


class Act1VAutoChessEffectType(CustomIntEnum):
    NONE = "NONE", 0
    BAND_INITIAL = "BAND_INITIAL", 1
    ENEMY = "ENEMY", 2
    ENEMY_TEMPORARY = "ENEMY_TEMPORARY", 3
    ALLY = "ALLY", 4
    EQUIP = "EQUIP", 5
    CHAR_MAP = "CHAR_MAP", 6
