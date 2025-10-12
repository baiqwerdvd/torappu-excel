from pydantic import BaseModel, ConfigDict

from .roguelike_buff import RoguelikeBuff


class RoguelikeRelicFeature(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    buffs: list[RoguelikeBuff]
