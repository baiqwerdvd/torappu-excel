from .return_price_item_data import ReturnPriceItemData
from ..common import BaseStruct


class ReturnPriceGroupData(BaseStruct):
    groupId: str
    content: list[ReturnPriceItemData]
