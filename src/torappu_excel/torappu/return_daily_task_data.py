from .mission_display_rewards import MissionDisplayRewards
from ..common import BaseStruct


class ReturnDailyTaskData(BaseStruct):
    groupId: str
    id: str
    groupSortId: int
    taskSortId: int
    template: str
    param: list[str]
    desc: str
    rewards: list[MissionDisplayRewards]
    playPoint: int
