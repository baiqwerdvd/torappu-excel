from .home_theme_limit_info_data import HomeThemeLimitInfoData
from ..common import BaseStruct

from msgspec import field


class HomeThemeLimitData(BaseStruct):
    id_: str = field(name="id")
    limitInfos: list[HomeThemeLimitInfoData]
