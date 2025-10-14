from pydantic import BaseModel, ConfigDict

from .mission_calc_state import MissionCalcState
from .mission_holding_state import MissionHoldingState


class MissionPlayerState(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    state: MissionHoldingState
    progress: list[MissionCalcState]
