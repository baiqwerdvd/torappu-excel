from pydantic import BaseModel, ConfigDict


class HomeThemeLimitInfoData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    startTime: int
    endTime: int
    invalidObtainDesc: str
