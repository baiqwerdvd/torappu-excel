from pydantic import BaseModel, ConfigDict

from .evolve_phase import EvolvePhase
from .rarity_rank import RarityRank


class Act1VHalfIdleCharMaxRankData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    rarity: RarityRank
    maxRankData: dict[str, "Act1VHalfIdleCharMaxRankData.MaxRankData"]
    maxEvolvePhase: EvolvePhase

    class MaxRankData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        evolvePhase: EvolvePhase
        maxLevel: int
        maxSkillRank: int
