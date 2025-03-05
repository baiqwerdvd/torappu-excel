from .item_bundle import ItemBundle
from ..common import BaseStruct


class Act4funMissionData(BaseStruct):
    missionId: str
    sortId: str
    missionDes: str
    rewardIconIds: list[str]
    rewards: list[ItemBundle]
