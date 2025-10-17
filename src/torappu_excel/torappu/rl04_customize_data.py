from .rl04_difficulty_ext import RL04DifficultyExt
from .rl04_ending_text import RL04EndingText
from .roguelike_common_development_data import RoguelikeCommonDevelopmentData
from ..common import BaseStruct


class RL04CustomizeData(BaseStruct):
    commonDevelopment: RoguelikeCommonDevelopmentData
    difficulties: list[RL04DifficultyExt]
    endingText: RL04EndingText
