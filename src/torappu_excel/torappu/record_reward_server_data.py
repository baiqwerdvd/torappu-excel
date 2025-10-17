from .item_bundle import ItemBundle
from ..common import BaseStruct


class RecordRewardServerData(BaseStruct):
    stageId: str
    rewards: list[ItemBundle]
