from pydantic import BaseModel, ConfigDict, Field


class RoguelikeGameZoneData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    name: str
    clockPerformance: str | None
    displayTime: str | None
    description: str
    endingDescription: str
    backgroundId: str
    zoneIconId: str
    isHiddenZone: bool
    bgmSignal: str
    bgmSignalWithLowSan: str | None
    buffDescription: str | None = Field(default=None)
