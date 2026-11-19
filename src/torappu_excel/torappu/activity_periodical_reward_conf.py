from .mission_display_rewards import MissionDisplayRewards
from ..common import BaseStruct


class ActivityPeriodicalRewardConf(BaseStruct):
    id: str
    periodicalPointCost: int
    sortIndex: int
    rewards: list[MissionDisplayRewards]
