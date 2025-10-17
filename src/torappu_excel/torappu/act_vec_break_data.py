from .act_vec_break_battle_buff_data import ActVecBreakBattleBuffData
from .act_vec_break_const_data import ActVecBreakConstData
from .act_vec_break_defense_stage_data import ActVecBreakDefenseStageData
from .act_vec_break_milestone_item_data import ActVecBreakMilestoneItemData
from .act_vec_break_offense_stage_data import ActVecBreakOffenseStageData
from .act_vec_break_zone_data import ActVecBreakZoneData
from ..common import BaseStruct


class ActVecBreakData(BaseStruct):
    offenseStageDict: dict[str, ActVecBreakOffenseStageData]
    defenseStageDict: dict[str, ActVecBreakDefenseStageData]
    milestoneList: list[ActVecBreakMilestoneItemData]
    battleBuffDict: dict[str, ActVecBreakBattleBuffData]
    constData: ActVecBreakConstData
    actZoneData: ActVecBreakZoneData
