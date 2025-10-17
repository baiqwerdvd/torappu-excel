from .sandbox_item_type import SandboxItemType
from ..common import BaseStruct


class SandboxRewardItemConfigData(BaseStruct):
    rewardItem: str
    rewardType: SandboxItemType
