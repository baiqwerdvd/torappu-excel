from pydantic import BaseModel, ConfigDict, Field


class ActArchiveEndbookItemData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    endBookId: str
    sortId: int
    endbookName: str
    unlockDesc: str
    textId: str
    enrollId: str | None = Field(default=None)
    isLast: bool | None = Field(default=None)
