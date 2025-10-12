from pydantic import BaseModel, ConfigDict

from .rl04_difficulty_ext import RL04DifficultyExt
from .rl04_ending_text import RL04EndingText
from .roguelike_common_development_data import RoguelikeCommonDevelopmentData


class RL04CustomizeData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    commonDevelopment: RoguelikeCommonDevelopmentData
    difficulties: list[RL04DifficultyExt]
    endingText: RL04EndingText
