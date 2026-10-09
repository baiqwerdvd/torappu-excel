from .roguelike_main_weather_data import RoguelikeMainWeatherData
from .roguelike_sub_weather_data import RoguelikeSubWeatherData
from ..common import BaseStruct


class RoguelikeWeatherModuleData(BaseStruct):
    mainWeatherData: dict[str, RoguelikeMainWeatherData]
    subWeatherData: dict[str, RoguelikeSubWeatherData]
