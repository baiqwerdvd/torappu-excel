from pydantic import BaseModel, ConfigDict

from .item_type import ItemType


class ReturnV2ItemData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    type: ItemType
    id: str
    count: int
    sortId: int
