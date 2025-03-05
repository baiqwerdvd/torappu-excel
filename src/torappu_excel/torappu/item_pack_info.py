from .item_bundle import ItemBundle
from ..common import BaseStruct


class ItemPackInfo(BaseStruct):
    packId: str
    content: list[ItemBundle]
