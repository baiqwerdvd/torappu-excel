from pydantic import BaseModel, ConfigDict


class OpenServerScheduleItem(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    versionId: str
    startTs: int
    endTs: int
    totalCheckinDescption: str
    chainLoginDescription: str
    charImg: str
