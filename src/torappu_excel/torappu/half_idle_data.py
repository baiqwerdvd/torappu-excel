from .act1_vhalf_idle_item_data import Act1VHalfIdleItemData
from ..common import BaseStruct


class HalfIdleData(BaseStruct):
    itemData: dict[str, Act1VHalfIdleItemData]
