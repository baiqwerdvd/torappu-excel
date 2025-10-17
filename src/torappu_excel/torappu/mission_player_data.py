from enum import IntEnum

from .mission_daily_rewards import MissionDailyRewards
from .mission_player_state import MissionPlayerState
from ..common import BaseStruct


class MissionPlayerData(BaseStruct):
    missions: dict[str, dict[str, MissionPlayerState]]
    missionRewards: MissionDailyRewards
    missionGroups: dict[str, "MissionPlayerData.MissionGroupState"]
    pinnedSpecialOperator: str

    class MissionGroupState(IntEnum):
        Uncomplete = 0
        Complete = 1
