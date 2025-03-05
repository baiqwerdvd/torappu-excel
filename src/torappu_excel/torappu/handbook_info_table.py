from .handbook_display_condition import HandbookDisplayCondition
from .handbook_info_data import HandbookInfoData
from .handbook_stage_time_data import HandbookStageTimeData
from .handbook_story_stage_data import HandbookStoryStageData
from .handbook_team_mission import HandbookTeamMission
from .npc_data import NPCData
from ..common import BaseStruct


class HandbookInfoTable(BaseStruct):
    handbookDict: dict[str, HandbookInfoData]
    npcDict: dict[str, NPCData]
    teamMissionList: dict[str, HandbookTeamMission]
    handbookDisplayConditionList: dict[str, HandbookDisplayCondition]
    handbookStageData: dict[str, HandbookStoryStageData]
    handbookStageTime: list[HandbookStageTimeData]
