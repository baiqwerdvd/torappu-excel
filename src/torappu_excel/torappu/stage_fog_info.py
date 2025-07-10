from .fog_type import FogType
from .item_type import ItemType
from .stage_button_in_fog_render_type import StageButtonInFogRenderType
from ..common import BaseStruct


class StageFogInfo(BaseStruct):
    lockId: str
    fogType: FogType
    stageButtonInFogRenderType: StageButtonInFogRenderType
    stageId: str
    lockName: str
    lockDesc: str
    unlockItemId: str
    unlockItemType: ItemType
    unlockItemNum: int
    preposedStageId: str
    preposedLockId: str | None
