from .return_mission_group_type import ReturnMissionGroupType
from .return_mission_item_data import ReturnMissionItemData
from ..common import BaseStruct


class ReturnMissionGroupData(BaseStruct):
    groupId: str
    sortId: int
    type: ReturnMissionGroupType
    missionList: list[ReturnMissionItemData]
