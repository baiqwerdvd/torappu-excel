from pydantic import BaseModel, ConfigDict

from .rarity_rank import RarityRank


class Act1VHalfIdleCharSkillRankData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    rarity: RarityRank
    skillRankData: list["Act1VHalfIdleCharSkillRankData.SkillRankData"]

    class SkillRankData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        skillLevel: int
        cost: int
        accumulatedCost: int
