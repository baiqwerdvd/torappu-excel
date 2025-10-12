from pydantic import BaseModel, ConfigDict

from .medal_per_data import MedalPerData
from .medal_type_data import MedalTypeData


class MedalData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    medalList: list[MedalPerData]
    medalTypeData: dict[str, MedalTypeData]
