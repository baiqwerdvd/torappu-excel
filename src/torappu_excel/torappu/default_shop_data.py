from pydantic import BaseModel, ConfigDict

from .item_bundle import ItemBundle


class DefaultShopData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    goodId: str
    slotId: int
    price: int
    availCount: int
    overrideName: str
    item: ItemBundle
