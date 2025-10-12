from pydantic import BaseModel, ConfigDict

from .mission_display_rewards import MissionDisplayRewards
from .mission_type import MissionType


class MissionGroup(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    title: str | None
    type: MissionType
    preMissionGroup: str | None
    period: list[int] | None
    rewards: list[MissionDisplayRewards] | None
    missionIds: list[str]
    startTs: int
    endTs: int
