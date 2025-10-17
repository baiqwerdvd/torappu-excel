from .home_background_limit_data import HomeBackgroundLimitData
from .home_background_single_data import HomeBackgroundSingleData
from .home_multi_form_info_data import HomeMultiFormInfoData
from .home_multi_form_time_rule_data import HomeMultiFormTimeRuleData
from .home_theme_display_data import HomeThemeDisplayData
from .home_theme_limit_data import HomeThemeLimitData
from ..common import BaseStruct


class HomeBackgroundData(BaseStruct):
    defaultBackgroundId: str
    defaultThemeId: str
    homeBgDataList: list[HomeBackgroundSingleData]
    themeList: list[HomeThemeDisplayData]
    backgroundLimitData: dict[str, HomeBackgroundLimitData]
    themeLimitData: dict[str, HomeThemeLimitData]
    multiFormInfoData: list[HomeMultiFormInfoData]
    timeRuleData: dict[str, list[HomeMultiFormTimeRuleData]]
    defaultBgMusicId: str
    themeStartTime: int
