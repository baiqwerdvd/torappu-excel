from enum import IntEnum

from .mission_daily_rewards import MissionDailyRewards
from .mission_player_state import MissionPlayerState
from ..common import BaseStruct


class MissionPlayerDataGroup(BaseStruct):
    MAIN: dict[str, MissionPlayerState]
    GUIDE: dict[str, MissionPlayerState]
    ACTIVITY: dict[str, MissionPlayerState]
    DAILY: dict[str, MissionPlayerState]
    WEEKLY: dict[str, MissionPlayerState]
    OPENSERVER: dict[str, MissionPlayerState]
    SUB: dict[str, MissionPlayerState]
    RETRO: dict[str, MissionPlayerState]
    SPECIAL_OPERATOR: dict[str, MissionPlayerState]
    SPECIAL_OPERATOR_WEEKLY: dict[str, MissionPlayerState]


class MissionPlayerData(BaseStruct):
    missions: MissionPlayerDataGroup
    missionRewards: MissionDailyRewards
    missionGroups: dict[str, "MissionPlayerData.MissionGroupState"]
    pinnedSpecialOperator: str

    class MissionGroupState(IntEnum):
        Uncomplete = 0
        Complete = 1
