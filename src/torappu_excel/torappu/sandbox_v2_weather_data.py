from .sandbox_v2_weather_type import SandboxV2WeatherType
from ..common import BaseStruct


class SandboxV2WeatherData(BaseStruct):
    weatherId: str
    name: str
    weatherLevel: int
    weatherType: SandboxV2WeatherType
    weatherTypeName: str
    weatherIconId: str
    functionDesc: str
    description: str
    buffId: str | None
