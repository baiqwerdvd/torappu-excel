from pydantic import BaseModel, ConfigDict


class SkinShopItemViewModel(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    goodId: str
    skinName: str
    skinId: str
    charId: str
    currencyUnit: str
    originPrice: int
    price: int
    discount: float | int
    desc1: str | None
    desc2: str | None
    startDateTime: int
    endDateTime: int
    slotId: int
    isRedeem: bool
