from .home_background_limit_info_data import HomeBackgroundLimitInfoData
from ..common import BaseStruct


class HomeBackgroundLimitData(BaseStruct):
    bgId: str
    limitInfos: list[HomeBackgroundLimitInfoData]
