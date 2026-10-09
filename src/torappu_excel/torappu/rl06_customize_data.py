from .rl06_difficulty_ext import RL06DifficultyExt
from .rl06_ending_text import RL06EndingText
from .roguelike_common_development_data import RoguelikeCommonDevelopmentData
from .roguelike_game_shop_dialog_data import RoguelikeGameShopDialogData
from ..common import BaseStruct


class RL06CustomizeData(BaseStruct):
    commonDevelopment: RoguelikeCommonDevelopmentData
    difficulties: list[RL06DifficultyExt]
    endingText: RL06EndingText
    scrapShopDialogData: RoguelikeGameShopDialogData
    employShopDialogData: RoguelikeGameShopDialogData
