from pydantic import BaseModel, ConfigDict

from .sandbox_v2_season_type import SandboxV2SeasonType


class SandboxV2SeasonData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    seasonType: SandboxV2SeasonType
    name: str
    functionDesc: str
    description: str
    color: str
