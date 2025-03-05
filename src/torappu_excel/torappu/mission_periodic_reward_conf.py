from .mission_display_rewards import MissionDisplayRewards
from .mission_type import MissionType
from ..common import BaseStruct

from msgspec import field


class MissionPeriodicRewardConf(BaseStruct):
    groupId: str
    id_: str = field(name="id")
    periodicalPointCost: int
    type_: MissionType = field(name="type")
    sortIndex: int
    rewards: list[MissionDisplayRewards]
