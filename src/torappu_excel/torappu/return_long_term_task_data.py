from .mission_display_rewards import MissionDisplayRewards
from ..common import BaseStruct

from msgspec import field


class ReturnLongTermTaskData(BaseStruct):
    id_: str = field(name="id")
    sortId: int
    template: str
    param: list[str]
    desc: str
    rewards: list[MissionDisplayRewards]
    playPoint: int
