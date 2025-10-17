from .sandbox_perm_item_type import SandboxPermItemType
from ..common import BaseStruct


class SandboxV2RewardItemConfigData(BaseStruct):
    rewardItem: str
    rewardType: SandboxPermItemType
