from .sandbox_perm_item_type import SandboxPermItemType
from .sandbox_v2_item_trap_tag import SandboxV2ItemTrapTag
from ..common import BaseStruct


class SandboxV2NodeUpgradeData(BaseStruct):
    nodeUpgradeId: str
    name: str
    description: str
    upgradeDesc: str
    upgradeTips: str
    itemType: SandboxPermItemType
    itemTag: SandboxV2ItemTrapTag
    itemCnt: int
    itemRarity: int
