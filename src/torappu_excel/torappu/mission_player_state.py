from .mission_calc_state import MissionCalcState
from .mission_holding_state import MissionHoldingState
from ..common import BaseStruct


class MissionPlayerState(BaseStruct):
    state: MissionHoldingState
    progress: list[MissionCalcState]
