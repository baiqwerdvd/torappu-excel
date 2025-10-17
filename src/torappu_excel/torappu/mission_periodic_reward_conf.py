from .mission_display_rewards import MissionDisplayRewards
from .mission_type import MissionType
from ..common import BaseStruct


class MissionPeriodicRewardConf(BaseStruct):
    groupId: str
    id: str
    periodicalPointCost: int
    type: MissionType
    sortIndex: int
    rewards: list[MissionDisplayRewards]
