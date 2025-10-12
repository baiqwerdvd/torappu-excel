from pydantic import BaseModel, ConfigDict

from .extra_shop_group_type import ExtraShopGroupType
from .item_bundle import ItemBundle


class ExtraQCObject(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    goodId: str
    item: ItemBundle
    displayName: str
    slotId: int
    originPrice: int
    price: int
    availCount: int
    discount: float | int
    goodEndTime: int
    shopType: ExtraShopGroupType
    newFlagTimeStamp: int
