from pydantic import BaseModel, ConfigDict

from .act_multi_v3_map_mode_type import ActMultiV3MapModeType


class ActMultiV3MapModeData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    modeType: ActMultiV3MapModeType
    name: str
    iconId: str
    color: str
    quickMatchSortId: int
    stageOverviewSortId: int
    unlockTs: int
    unlockPageTitle: str
    unlockPageDesc: str
