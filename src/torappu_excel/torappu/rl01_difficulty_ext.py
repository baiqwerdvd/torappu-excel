from pydantic import BaseModel, ConfigDict

from .roguelike_topic_mode import RoguelikeTopicMode


class RL01DifficultyExt(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    modeDifficulty: RoguelikeTopicMode
    grade: int
    buffDesc: list[str]
