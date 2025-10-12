from pydantic import BaseModel, ConfigDict


class ActArchiveTrapItemData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    trapId: str
    trapSortId: int
    orderId: str
    enrollId: str | None
