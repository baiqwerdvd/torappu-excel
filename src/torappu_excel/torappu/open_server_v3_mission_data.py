from .mission_display_rewards import MissionDisplayRewards
from .mission_type import MissionType
from .open_server_mission_type import OpenServerMissionType
from .open_server_v3_jump_type import OpenServerV3JumpType
from ..common import BaseStruct


class OpenServerV3MissionData(BaseStruct):
    id: str
    sortId: int
    description: str
    type: MissionType
    openServerMissionType: OpenServerMissionType
    missionGroup: str
    jumpType: OpenServerV3JumpType
    jumpPlace: str | None
    rewards: list[MissionDisplayRewards]
