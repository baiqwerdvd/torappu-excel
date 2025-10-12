from pydantic import BaseModel, ConfigDict


class ActArchiveChaosItemData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    isHidden: bool
    enrollId: str | None
    sortId: int
