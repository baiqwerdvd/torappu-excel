from pydantic import BaseModel, ConfigDict


class ZoneRecordUnlockData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    noteId: str
    zoneId: str
    initialName: str
    finalName: str | None
    accordingExposeId: str | None
    initialDes: str
    finalDes: str | None
    remindDes: str | None
