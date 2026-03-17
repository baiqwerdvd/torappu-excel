from .sticker_item_data import StickerItemData
from ..common import BaseStruct


class StickerData(BaseStruct):
    stickerMap: dict[str, StickerItemData]
