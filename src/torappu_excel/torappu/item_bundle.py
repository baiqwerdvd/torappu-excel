from pydantic import BaseModel, ConfigDict

from .item_type import ItemType


class ItemBundle(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    count: int
    type: ItemType
