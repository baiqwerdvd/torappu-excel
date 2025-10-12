from pydantic import BaseModel, ConfigDict

from .roguelike_topic_mode import RoguelikeTopicMode


class RoguelikeDicePredefineData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    modeId: RoguelikeTopicMode
    modeGrade: int
    predefinedId: str | None
    initialDiceCount: int
