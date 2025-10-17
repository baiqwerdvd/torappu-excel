from .return_v2_mission_item_data import ReturnV2MissionItemData
from ..common import BaseStruct


class ReturnV2MissionGroupData(BaseStruct):
    groupId: str
    sortId: int
    tabTitle: str
    title: str
    desc: str
    diffMissionCount: int
    startTime: int
    endTime: int
    imageId: str
    iconId: str
    missionList: list[ReturnV2MissionItemData]
