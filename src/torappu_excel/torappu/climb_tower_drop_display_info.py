from pydantic import BaseModel, ConfigDict

from .item_type import ItemType


class ClimbTowerDropDisplayInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    itemId: str
    type: ItemType
    maxCount: int
    minCount: int
