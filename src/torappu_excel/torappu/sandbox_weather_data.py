from pydantic import BaseModel, ConfigDict

from .sandbox_weather_type import SandboxWeatherType


class SandboxWeatherData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    weatherId: str
    weatherType: SandboxWeatherType
    weatherLevel: int
    name: str
    description: str
    weatherTypeName: str
    weatherTypeIconId: str
    functionDesc: str
    buffId: str
