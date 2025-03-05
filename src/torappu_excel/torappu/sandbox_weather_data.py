from .sandbox_weather_type import SandboxWeatherType
from ..common import BaseStruct


class SandboxWeatherData(BaseStruct):
    weatherId: str
    weatherType: SandboxWeatherType
    weatherLevel: int
    name: str
    description: str
    weatherTypeName: str
    weatherTypeIconId: str
    functionDesc: str
    buffId: str
