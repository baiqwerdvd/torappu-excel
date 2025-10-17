from .mission_calc_state import MissionCalcState
from ..common import BaseStruct


class PlayerHiddenStage(BaseStruct):
    missions: list[MissionCalcState]
    unlock: int
