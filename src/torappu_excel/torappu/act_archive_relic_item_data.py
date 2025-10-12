from pydantic import BaseModel, ConfigDict


class ActArchiveRelicItemData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    relicId: str
    relicSortId: int
    relicGroupId: int
    orderId: str
    isSpRelic: bool
    enrollId: str | None
