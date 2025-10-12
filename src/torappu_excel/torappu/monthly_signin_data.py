from pydantic import BaseModel, ConfigDict

from .item_type import ItemType


class MonthlySignInData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    itemId: str
    itemType: ItemType
    count: int
