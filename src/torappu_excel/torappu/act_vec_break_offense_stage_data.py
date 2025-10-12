from pydantic import BaseModel, ConfigDict, Field

from .act_vec_break_offense_boss_data import ActVecBreakOffenseBossData
from .act_vec_break_particle_type import ActVecBreakParticleType
from .item_bundle import ItemBundle


class ActVecBreakOffenseStageData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    stageId: str
    level: int
    storyDesc: str
    particleType: ActVecBreakParticleType
    firstReward: ItemBundle
    commonReward: ItemBundle
    bossData: ActVecBreakOffenseBossData | None = Field(default=None)
