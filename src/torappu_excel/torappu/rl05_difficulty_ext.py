from pydantic import BaseModel, ConfigDict

from .roguelike_topic_mode import RoguelikeTopicMode


class RL05DifficultyExt(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    modeDifficulty: RoguelikeTopicMode
    grade: int
    buffs: list[str] | None
    buffDesc: list[str]
    leftWrathDesc: str
    relicDevLevel: str
    gildProbDisplay: str
    skyStepDescription: str
