from .act_archive_weather_item_data import ActArchiveWeatherItemData
from ..common import BaseStruct


class ActArchiveWeatherData(BaseStruct):
    weathers: dict[str, ActArchiveWeatherItemData]
