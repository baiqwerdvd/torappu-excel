from pydantic import BaseModel, ConfigDict

from .act_vec_break_v2_boss_data import ActVecBreakV2BossData
from .act_vec_break_v2_stage_order_type import ActVecBreakV2StageOrderType


class ActVecBreakV2HardStageData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    stageId: str
    orderType: ActVecBreakV2StageOrderType
    storyDesc: str
    bossData: ActVecBreakV2BossData | None
