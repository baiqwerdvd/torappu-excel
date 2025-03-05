from .item_bundle import ItemBundle
from ..common import BaseStruct


class NewbieCheckInPackageRewardData(BaseStruct):
    orderNum: int
    itemBundle: ItemBundle
