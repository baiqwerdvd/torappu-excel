from .player_training_camp_stage import PlayerTrainingCampStage
from ..common import BaseStruct


class PlayerTrainingCamp(BaseStruct):
    stages: dict[str, PlayerTrainingCampStage]
