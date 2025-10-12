from pydantic import BaseModel, ConfigDict


class CashShopObject(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    goodId: str
    slotId: int
    price: int
    diamondNum: int
    doubleCount: int
    plusNum: int
    desc: str
