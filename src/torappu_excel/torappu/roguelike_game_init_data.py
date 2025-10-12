from pydantic import BaseModel, ConfigDict

from .roguelike_topic_mode import RoguelikeTopicMode


class RoguelikeGameInitData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    modeId: RoguelikeTopicMode
    modeGrade: int
    predefinedId: str | None
    predefinedStyle: str | None
    initialBandRelic: list[str]
    initialRecruitGroup: list[str] | None
    initialHp: int
    initialPopulation: int
    initialGold: int
    initialSquadCapacity: int
    initialShield: int
    initialMaxHp: int
    initialKey: int
