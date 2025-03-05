from .fog_type import FogType
from .item_type import ItemType
from ..common import BaseStruct


class StageFogInfo(BaseStruct):
    lockId: str
    fogType: FogType
    stageId: str
    lockName: str
    lockDesc: str
    unlockItemId: str
    unlockItemType: ItemType
    unlockItemNum: int
    preposedStageId: str
    preposedLockId: str | None
