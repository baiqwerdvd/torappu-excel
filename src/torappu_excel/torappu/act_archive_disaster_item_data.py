from pydantic import BaseModel, ConfigDict


class ActArchiveDisasterItemData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    disasterId: str
    sortId: int
    enrollConditionId: str | None
    picSmallId: str
    picBigActiveId: str
    picBigInactiveId: str
