from pydantic import BaseModel, ConfigDict

from .act_vec_break_v2_boss_data import ActVecBreakV2BossData
from .act_vec_break_v2_particle_type import ActVecBreakV2ParticleType


class ActVecBreakV2OffenseStageData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    stageId: str
    level: int
    levelLayout: str
    storyDesc: str
    particleType: ActVecBreakV2ParticleType
    bossData: ActVecBreakV2BossData | None
