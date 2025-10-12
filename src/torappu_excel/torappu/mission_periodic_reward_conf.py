from pydantic import BaseModel, ConfigDict

from .mission_display_rewards import MissionDisplayRewards
from .mission_type import MissionType


class MissionPeriodicRewardConf(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    groupId: str
    id: str
    periodicalPointCost: int
    type: MissionType
    sortIndex: int
    rewards: list[MissionDisplayRewards]
