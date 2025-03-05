from .item_bundle import ItemBundle
from ..common import BaseStruct


class ActivityLoginData(BaseStruct):
    description: str
    itemList: list[ItemBundle]
    apSupplyOutOfDateDict: dict[str, int]
