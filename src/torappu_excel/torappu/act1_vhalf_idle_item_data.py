from pydantic import BaseModel, ConfigDict

from .act1_vhalf_idle_item_type import Act1VHalfIdleItemType


class Act1VHalfIdleItemData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    actId: str
    itemId: str
    itemType: Act1VHalfIdleItemType
    itemName: str
    sortId: int
    iconId: str
    funcDesc: str
    flavorDesc: str
    obtainApproach: str
    showInInventory: bool
