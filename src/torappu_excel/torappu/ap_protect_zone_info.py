from pydantic import BaseModel, ConfigDict


class ApProtectZoneInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    zoneId: str
    timeRanges: list["ApProtectZoneInfo.TimeRange"]

    class TimeRange(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        startTs: int
        endTs: int
