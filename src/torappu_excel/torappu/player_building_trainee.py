from .player_building_trainee_state import PlayerBuildingTraineeState
from ..common import BaseStruct


class PlayerBuildingTrainee(BaseStruct):
    state: PlayerBuildingTraineeState
    charInstId: int
    processPoint: float
    speed: float
    targetSkill: int
