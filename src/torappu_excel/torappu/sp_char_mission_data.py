from .item_bundle import ItemBundle
from .sp_char_mission_cond_type import SpCharMissionCondType
from ..common import BaseStruct


class SpCharMissionData(BaseStruct):
    charId: str
    missionId: str
    sortId: int
    condType: SpCharMissionCondType
    param: list[str]
    rewards: list[ItemBundle]
