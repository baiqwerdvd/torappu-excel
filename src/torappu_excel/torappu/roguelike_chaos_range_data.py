from pydantic import BaseModel, ConfigDict

from .chaos_effect_rank import ChaosEffectRank


class RoguelikeChaosRangeData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    chaosMax: int
    chaosDungeonEffect: ChaosEffectRank
