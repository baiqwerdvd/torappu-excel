from .player_building_trainer_state import PlayerBuildingTrainerState
from ..common import BaseStruct


class PlayerBuildingTrainer(BaseStruct):
    state: PlayerBuildingTrainerState
    charInstId: int
