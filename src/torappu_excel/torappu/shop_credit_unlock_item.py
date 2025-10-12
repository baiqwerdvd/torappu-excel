from pydantic import BaseModel, ConfigDict


class ShopCreditUnlockItem(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    sortId: int
    unlockNum: int
    charId: str
