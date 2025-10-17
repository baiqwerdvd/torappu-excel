from .home_theme_limit_info_data import HomeThemeLimitInfoData
from ..common import BaseStruct


class HomeThemeLimitData(BaseStruct):
    id: str
    limitInfos: list[HomeThemeLimitInfoData]
