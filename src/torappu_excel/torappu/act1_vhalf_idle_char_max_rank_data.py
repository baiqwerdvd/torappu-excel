from .evolve_phase import EvolvePhase
from .rarity_rank import RarityRank
from ..common import BaseStruct


class Act1VHalfIdleCharMaxRankData(BaseStruct):
    rarity: RarityRank
    maxRankData: dict[str, "Act1VHalfIdleCharMaxRankData.MaxRankData"]
    maxEvolvePhase: EvolvePhase

    class MaxRankData(BaseStruct):
        evolvePhase: EvolvePhase
        maxLevel: int
        maxSkillRank: int
