from pydantic import BaseModel, ConfigDict

from .sandbox_perm_item_type import SandboxPermItemType
from .sandbox_v2_item_trap_tag import SandboxV2ItemTrapTag


class SandboxV2NodeUpgradeData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    nodeUpgradeId: str
    name: str
    description: str
    upgradeDesc: str
    upgradeTips: str
    itemType: SandboxPermItemType
    itemTag: SandboxV2ItemTrapTag
    itemCnt: int
    itemRarity: int
