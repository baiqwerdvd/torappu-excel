from .charm_item_data import CharmItemData
from ..common import BaseStruct


class CharmData(BaseStruct):
    charmList: list[CharmItemData]
