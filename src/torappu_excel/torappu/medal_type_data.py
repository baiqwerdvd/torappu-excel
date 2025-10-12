from pydantic import BaseModel, ConfigDict

from .medal_group_data import MedalGroupData


class MedalTypeData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    medalGroupId: str
    sortId: int
    medalName: str
    groupData: list[MedalGroupData]
