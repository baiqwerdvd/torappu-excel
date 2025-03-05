from .mission_display_rewards import MissionDisplayRewards
from ..common import BaseStruct

from msgspec import field


class ReturnDailyTaskData(BaseStruct):
    groupId: str
    id_: str = field(name="id")
    groupSortId: int
    taskSortId: int
    template: str
    param: list[str]
    desc: str
    rewards: list[MissionDisplayRewards]
    playPoint: int
