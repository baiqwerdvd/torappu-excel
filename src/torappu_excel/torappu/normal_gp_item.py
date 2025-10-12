from pydantic import BaseModel, ConfigDict, Field

from .item_bundle import ItemBundle
from .shop_currency_unit import ShopCurrencyUnit
from .special_item_info import SpecialItemInfo


class GPShopNormalGPItem(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    goodId: str
    giftPackageId: str
    priority: int
    displayName: str
    currencyUnit: ShopCurrencyUnit
    availCount: int
    price: int
    originPrice: int
    discount: float | int
    items: list[ItemBundle]
    specialItemInfos: dict[str, SpecialItemInfo]
    startDateTime: int = Field(default=0)
    endDateTime: int = Field(default=0)
    groupId: str | None = Field(default=None)
    buyCount: int | None = Field(default=None)
