from .mission_display_rewards import MissionDisplayRewards
from .mission_type import MissionType
from ..common import BaseStruct


class MissionGroup(BaseStruct):
    id: str
    title: str | None
    type: MissionType
    preMissionGroup: str | None
    period: list[int] | None
    rewards: list[MissionDisplayRewards] | None
    missionIds: list[str]
    startTs: int
    endTs: int
