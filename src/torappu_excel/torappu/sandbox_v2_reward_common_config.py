from .sandbox_perm_item_type import SandboxPermItemType
from ..common import BaseStruct


class SandboxV2RewardCommonConfig(BaseStruct):
    rewardItemId: str
    rewardItemType: SandboxPermItemType
    count: int
