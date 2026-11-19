from .open_server_mission_type import OpenServerMissionType
from ..common import BaseStruct


class OpenServerV3MissionTypeDescData(BaseStruct):
    missionType: OpenServerMissionType
    desc: str
