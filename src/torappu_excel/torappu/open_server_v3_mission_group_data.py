from .mission_display_rewards import MissionDisplayRewards
from .mission_type import MissionType
from ..common import BaseStruct


class OpenServerV3MissionGroupData(BaseStruct):
    id: str
    type: MissionType
    sortId: int
    title: str
    period: list[int] | None
    rewards: list[MissionDisplayRewards]
    startTs: int
    endTs: int
