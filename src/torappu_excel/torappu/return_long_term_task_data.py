from .mission_display_rewards import MissionDisplayRewards
from ..common import BaseStruct


class ReturnLongTermTaskData(BaseStruct):
    id: str
    sortId: int
    template: str
    param: list[str]
    desc: str
    rewards: list[MissionDisplayRewards]
    playPoint: int
