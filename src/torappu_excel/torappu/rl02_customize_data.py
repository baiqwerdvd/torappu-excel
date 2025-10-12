from pydantic import BaseModel, ConfigDict

from .rl02_dev_raw_text_buff_group import RL02DevRawTextBuffGroup
from .rl02_development import RL02Development
from .rl02_development_line import RL02DevelopmentLine
from .rl02_difficulty_ext import RL02DifficultyExt
from .rl02_ending_text import RL02EndingText
from .roguelike_topic_dev_token import RoguelikeTopicDevToken


class RL02CustomizeData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    developments: dict[str, RL02Development]
    developmentTokens: dict[str, RoguelikeTopicDevToken]
    developmentRawTextGroup: list[RL02DevRawTextBuffGroup]
    developmentLines: list[RL02DevelopmentLine]
    endingText: RL02EndingText
    difficulties: list[RL02DifficultyExt]
