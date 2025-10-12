from pydantic import BaseModel, ConfigDict

from .san_effect_rank import SanEffectRank


class RoguelikeSanRangeData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    sanMax: int
    diceGroupId: str
    description: str
    sanDungeonEffect: SanEffectRank
    sanEffectRank: SanEffectRank
    sanEndingDesc: str | None
