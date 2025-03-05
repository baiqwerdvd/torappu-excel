from .item_bundle import ItemBundle
from ..common import BaseStruct


class SandboxV2ChallengeModeRewardData(BaseStruct):
    rewardId: str
    sortId: int
    rewardDay: int
    rewardItemList: list[ItemBundle]
