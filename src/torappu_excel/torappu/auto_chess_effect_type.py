from enum import StrEnum


class AutoChessEffectType(StrEnum):
    NONE = "NONE"
    BAND_INITIAL = "BAND_INITIAL"
    ENEMY = "ENEMY"
    ENEMY_TEMPORARY = "ENEMY_TEMPORARY"
    ALLY = "ALLY"
    EQUIP = "EQUIP"
    MAGIC = "MAGIC"
    CHAR_MAP = "CHAR_MAP"
    BOND = "BOND"
    ENEMY_GAIN = "ENEMY_GAIN"
    BUFF_GAIN = "BUFF_GAIN"
    GARRISON = "GARRISON"
