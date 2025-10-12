from pydantic import BaseModel, ConfigDict

from .roguelike_outer_buff import RoguelikeOuterBuff


class RoguelikeOutBuffData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    buffs: dict[str, RoguelikeOuterBuff]
