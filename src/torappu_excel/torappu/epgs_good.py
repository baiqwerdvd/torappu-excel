from pydantic import BaseModel, ConfigDict, Field

from .item_bundle import ItemBundle


class EPGSGood(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    goodId: str
    goodType: str
    startTime: int
    availCount: int
    item: ItemBundle
    price: int
    sortId: int
    endTime: int | None = Field(default=None)
