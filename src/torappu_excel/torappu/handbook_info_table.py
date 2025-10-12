from pydantic import BaseModel, ConfigDict

from .handbook_display_condition import HandbookDisplayCondition
from .handbook_info_data import HandbookInfoData
from .handbook_stage_time_data import HandbookStageTimeData
from .handbook_story_stage_data import HandbookStoryStageData
from .handbook_team_mission import HandbookTeamMission
from .npc_data import NPCData


class HandbookInfoTable(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    handbookDict: dict[str, HandbookInfoData]
    npcDict: dict[str, NPCData]
    teamMissionList: dict[str, HandbookTeamMission]
    handbookDisplayConditionList: dict[str, HandbookDisplayCondition]
    handbookStageData: dict[str, HandbookStoryStageData]
    handbookStageTime: list[HandbookStageTimeData]
