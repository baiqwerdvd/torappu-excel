from pydantic import BaseModel, ConfigDict

from .shop_credit_unlock_item import ShopCreditUnlockItem


class ShopCreditUnlockGroup(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    index: str
    startDateTime: int
    charDict: list[ShopCreditUnlockItem]
