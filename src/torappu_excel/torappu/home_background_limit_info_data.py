from pydantic import BaseModel, ConfigDict


class HomeBackgroundLimitInfoData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    limitInfoId: str
    startTime: int
    endTime: int
    invalidObtainDesc: str
    displayAfterEndTime: bool
