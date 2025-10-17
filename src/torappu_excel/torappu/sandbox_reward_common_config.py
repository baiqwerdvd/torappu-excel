from .sandbox_item_type import SandboxItemType
from ..common import BaseStruct


class SandboxRewardCommonConfig(BaseStruct):
    rewardItemId: str
    rewardItemType: SandboxItemType
    count: int
