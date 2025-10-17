from .item_bundle import ItemBundle
from ..common import BaseStruct


class ReturnCheckinData(BaseStruct):
    isImportant: bool
    checkinRewardItems: list[ItemBundle]
