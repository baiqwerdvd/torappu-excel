from pydantic import BaseModel, ConfigDict

from .act_multi_v3_map_mode_type import ActMultiV3MapModeType


class ActMultiV3SquadInfoData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    sortId: int
    name: str
    modeType: ActMultiV3MapModeType
