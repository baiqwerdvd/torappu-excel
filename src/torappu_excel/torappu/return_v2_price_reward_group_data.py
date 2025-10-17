from .return_v2_price_reward_data import ReturnV2PriceRewardData
from ..common import BaseStruct


class ReturnV2PriceRewardGroupData(BaseStruct):
    groupId: str
    startTime: int
    endTime: int
    contentList: list[ReturnV2PriceRewardData]
