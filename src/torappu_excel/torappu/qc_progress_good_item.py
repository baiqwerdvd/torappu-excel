from pydantic import BaseModel, ConfigDict

from .item_bundle import ItemBundle


class QCProgressGoodItem(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    order: int
    price: int
    displayName: str
    item: ItemBundle
