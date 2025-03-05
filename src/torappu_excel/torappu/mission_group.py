from .mission_display_rewards import MissionDisplayRewards
from .mission_type import MissionType
from ..common import BaseStruct

from msgspec import field


class MissionGroup(BaseStruct):
    id_: str = field(name="id")
    title: str | None
    type_: MissionType = field(name="type")
    preMissionGroup: str | None
    period: list[int] | None
    rewards: list[MissionDisplayRewards] | None
    missionIds: list[str]
    startTs: int
    endTs: int
