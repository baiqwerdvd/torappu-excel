from .act_ark_hub_item_type import ActArkHubItemType
from ..common import BaseStruct


class ActArkHubRewardItem(BaseStruct):
    itemId: str
    count: int
    itemType: ActArkHubItemType
