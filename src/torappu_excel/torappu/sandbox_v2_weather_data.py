from pydantic import BaseModel, ConfigDict

from .sandbox_v2_weather_type import SandboxV2WeatherType


class SandboxV2WeatherData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    weatherId: str
    name: str
    weatherLevel: int
    weatherType: SandboxV2WeatherType
    weatherTypeName: str
    weatherIconId: str
    functionDesc: str
    description: str
    buffId: str | None
