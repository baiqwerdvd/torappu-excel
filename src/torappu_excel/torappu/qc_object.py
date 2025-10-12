from pydantic import BaseModel, ConfigDict, Field

from .item_bundle import ItemBundle
from .shop_qc_good_type import ShopQCGoodType


class QCObject(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    goodId: str
    item: ItemBundle | None
    progressGoodId: str | None
    displayName: str | None
    originPrice: int
    price: int
    availCount: int
    discount: float | int
    priority: int
    number: int
    goodStartTime: int
    goodEndTime: int
    goodType: ShopQCGoodType
    slotId: int | None = Field(default=None)
