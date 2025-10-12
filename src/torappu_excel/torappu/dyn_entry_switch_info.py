from pydantic import BaseModel, ConfigDict


class DynEntrySwitchInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    entryId: str
    sortId: int
    stageId: str | None
    signalId: str | None
