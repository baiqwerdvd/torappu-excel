from .act_vec_break_v2_boss_data import ActVecBreakV2BossData
from .act_vec_break_v2_particle_type import ActVecBreakV2ParticleType
from ..common import BaseStruct


class ActVecBreakV2OffenseStageData(BaseStruct):
    stageId: str
    level: int
    levelLayout: str
    storyDesc: str
    particleType: ActVecBreakV2ParticleType
    bossData: ActVecBreakV2BossData | None
