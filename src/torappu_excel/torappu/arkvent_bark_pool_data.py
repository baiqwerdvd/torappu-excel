from .arkvent_bark_item_data import ArkventBarkItemData
from ..common import BaseStruct


class ArkventBarkPoolData(BaseStruct):
    barkItemData: list[ArkventBarkItemData]
