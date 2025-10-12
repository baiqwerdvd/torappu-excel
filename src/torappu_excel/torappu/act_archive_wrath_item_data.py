from pydantic import BaseModel, ConfigDict


class ActArchiveWrathItemData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    wrathId: str
    sortId: int
    picTitleId: str
    picSmallInactiveId: str | None
    picSmallActiveId: str
    picBigActiveId: str
    picBigInactiveId: str | None
    enrollId: str | None
    isSp: bool
