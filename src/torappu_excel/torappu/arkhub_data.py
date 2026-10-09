from .act_ark_hub_item_data import ActArkHubItemData
from ..common import BaseStruct


class ArkhubData(BaseStruct):
    itemData: dict[str, ActArkHubItemData]
