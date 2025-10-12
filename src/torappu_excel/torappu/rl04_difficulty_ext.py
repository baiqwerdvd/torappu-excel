from pydantic import BaseModel, ConfigDict

from .roguelike_topic_mode import RoguelikeTopicMode


class RL04DifficultyExt(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    modeDifficulty: RoguelikeTopicMode
    grade: int
    leftDisasterDesc: str
    leftOverweightDesc: str
    relicDevLevel: str
    weightStatusLimitDesc: str
    buffs: list[str] | None
    buffDesc: list[str]
