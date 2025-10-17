from .act_vec_break_v2_boss_data import ActVecBreakV2BossData
from .act_vec_break_v2_stage_order_type import ActVecBreakV2StageOrderType
from ..common import BaseStruct


class ActVecBreakV2HardStageData(BaseStruct):
    stageId: str
    orderType: ActVecBreakV2StageOrderType
    storyDesc: str
    bossData: ActVecBreakV2BossData | None
