from pydantic import BaseModel, ConfigDict

from .rl01_difficulty_ext import RL01DifficultyExt
from .rl01_ending_text import RL01EndingText
from .roguelike_topic_dev import RoguelikeTopicDev
from .roguelike_topic_dev_token import RoguelikeTopicDevToken


class RL01CustomizeData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    developments: dict[str, RoguelikeTopicDev]
    developmentTokens: dict[str, RoguelikeTopicDevToken]
    endingText: RL01EndingText
    difficulties: list[RL01DifficultyExt]
