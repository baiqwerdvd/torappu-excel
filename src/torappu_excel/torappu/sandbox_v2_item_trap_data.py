from .sandbox_v2_item_trap_tag import SandboxV2ItemTrapTag
from .sandbox_v2_trap_item_type import SandboxV2TrapItemType
from ..common import BaseStruct


class SandboxV2ItemTrapData(BaseStruct):
    itemId: str
    trapId: str
    trapPhase: int
    trapLevel: int
    skillIndex: int
    skillLevel: int
    buildingLevel: int
    updatedItemId: str | None
    minLevelItemId: str
    baseItemName: str
    itemType: SandboxV2TrapItemType
    itemTag: SandboxV2ItemTrapTag
    buffId: str | None
