from pydantic import BaseModel, ConfigDict

from .stage_data import StageData


class TimelyDropInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    dropInfo: dict[str, StageData.StageDropInfo]
