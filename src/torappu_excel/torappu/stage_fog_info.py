from pydantic import BaseModel, ConfigDict

from .fog_type import FogType
from .item_type import ItemType
from .stage_button_in_fog_render_type import StageButtonInFogRenderType


class StageFogInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

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
