from pydantic import BaseModel, ConfigDict

from .rl05_difficulty_ext import RL05DifficultyExt
from .rl05_ending_text import RL05EndingText
from .roguelike_common_development_data import RoguelikeCommonDevelopmentData
from .roguelike_game_shop_dialog_data import RoguelikeGameShopDialogData


class RL05CustomizeData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    commonDevelopment: RoguelikeCommonDevelopmentData
    difficulties: list[RL05DifficultyExt]
    specialShopDialog: RoguelikeGameShopDialogData
    endingText: RL05EndingText
