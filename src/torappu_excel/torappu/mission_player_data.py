from enum import IntEnum

from pydantic import BaseModel, ConfigDict

from .mission_daily_rewards import MissionDailyRewards
from .mission_player_state import MissionPlayerState


class MissionPlayerData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    missions: dict[str, dict[str, MissionPlayerState]]
    missionRewards: MissionDailyRewards
    missionGroups: dict[str, "MissionPlayerData.MissionGroupState"]
    pinnedSpecialOperator: str

    class MissionGroupState(IntEnum):
        Uncomplete = 0
        Complete = 1
