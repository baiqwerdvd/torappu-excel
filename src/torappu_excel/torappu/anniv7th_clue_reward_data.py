from .item_bundle import ItemBundle
from ..common import BaseStruct


class Anniv7thClueRewardData(BaseStruct):
    clueRecordId: str
    clueRecord: int
    clueRecordDesc: str
    rewards: list[ItemBundle]
