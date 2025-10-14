from pydantic import BaseModel, ConfigDict

from .item_type import ItemType


class PlayerBuildingShopOutputItem(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    type: ItemType
    count: int
