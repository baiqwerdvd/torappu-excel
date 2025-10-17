from .rarity_rank import RarityRank
from ..common import BaseStruct


class Act1VHalfIdleCharSkillRankData(BaseStruct):
    rarity: RarityRank
    skillRankData: list["Act1VHalfIdleCharSkillRankData.SkillRankData"]

    class SkillRankData(BaseStruct):
        skillLevel: int
        cost: int
        accumulatedCost: int
