from pydantic import BaseModel, ConfigDict

from .act_vec_break_v2_battle_buff_data import ActVecBreakV2BattleBuffData
from .act_vec_break_v2_const_data import ActVecBreakV2ConstData
from .act_vec_break_v2_defense_basic_data import ActVecBreakV2DefenseBasicData
from .act_vec_break_v2_defense_detail_data import ActVecBreakV2DefenseDetailData
from .act_vec_break_v2_defense_group_data import ActVecBreakV2DefenseGroupData
from .act_vec_break_v2_hard_stage_data import ActVecBreakV2HardStageData
from .act_vec_break_v2_milestone_item_data import ActVecBreakV2MilestoneItemData
from .act_vec_break_v2_offense_stage_data import ActVecBreakV2OffenseStageData
from .act_vec_break_v2_schedule_block_data import ActVecBreakV2ScheduleBlockData
from .act_vec_break_v2_stage_reward_data import ActVecBreakV2StageRewardData
from .act_vec_break_v2_zone_data import ActVecBreakV2ZoneData


class ActVecBreakV2Data(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    offenseStageDict: dict[str, ActVecBreakV2OffenseStageData]
    hardStageDict: dict[str, ActVecBreakV2HardStageData]
    defenseBasicDict: dict[str, ActVecBreakV2DefenseBasicData]
    defenseDetailDict: dict[str, ActVecBreakV2DefenseDetailData]
    zoneDict: dict[str, ActVecBreakV2ZoneData]
    defenseGroupDict: dict[str, ActVecBreakV2DefenseGroupData]
    battleBuffDict: dict[str, ActVecBreakV2BattleBuffData]
    milestoneList: list[ActVecBreakV2MilestoneItemData]
    stageRewardDict: dict[str, ActVecBreakV2StageRewardData]
    constData: ActVecBreakV2ConstData
    squadBuffAvailStageList: list[str]
    scheduleBlockList: list[ActVecBreakV2ScheduleBlockData]
    defenseZoneId: str
    offenseZoneId: str
    hardZoneId: str
    firstDefenseGroupId: str
