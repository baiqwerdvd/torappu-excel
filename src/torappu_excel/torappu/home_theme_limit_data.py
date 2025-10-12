from pydantic import BaseModel, ConfigDict

from .home_theme_limit_info_data import HomeThemeLimitInfoData


class HomeThemeLimitData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    limitInfos: list[HomeThemeLimitInfoData]
