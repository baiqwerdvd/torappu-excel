from .act_vec_break_offense_boss_data import ActVecBreakOffenseBossData
from .act_vec_break_particle_type import ActVecBreakParticleType
from .item_bundle import ItemBundle
from ..common import BaseStruct

from msgspec import field


class ActVecBreakOffenseStageData(BaseStruct):
    stageId: str
    level: int
    storyDesc: str
    particleType: ActVecBreakParticleType
    firstReward: ItemBundle
    commonReward: ItemBundle
    bossData: ActVecBreakOffenseBossData | None = field(default=None)
