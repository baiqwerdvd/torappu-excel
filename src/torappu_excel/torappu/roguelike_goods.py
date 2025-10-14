from pydantic import BaseModel, ConfigDict


class RoguelikeGoods(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    index: str
    itemId: str
    count: int
    priceId: str
    priceCount: int
