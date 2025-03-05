from enum import StrEnum

from ..common import BaseStruct


class LevelData(BaseStruct):
    class Difficulty(StrEnum):
        NONE = "NONE"
        NORMAL = "NORMAL"
        FOUR_STAR = "FOUR_STAR"
        EASY = "EASY"
        ALL = "ALL"
