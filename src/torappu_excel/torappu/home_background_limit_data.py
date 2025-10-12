from pydantic import BaseModel, ConfigDict

from .home_background_limit_info_data import HomeBackgroundLimitInfoData


class HomeBackgroundLimitData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    bgId: str
    limitInfos: list[HomeBackgroundLimitInfoData]
