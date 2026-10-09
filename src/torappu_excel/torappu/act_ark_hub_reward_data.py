from .act_ark_hub_reward_item import ActArkHubRewardItem
from ..common import BaseStruct


class ActArkHubRewardData(BaseStruct):
    rewardId: str
    itemList: list[ActArkHubRewardItem]
