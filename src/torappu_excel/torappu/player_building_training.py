from pydantic import BaseModel, ConfigDict

from .date_time import DateTime
from .player_building_trainee import PlayerBuildingTrainee
from .player_building_trainer import PlayerBuildingTrainer
from .player_building_training_buff import PlayerBuildingTrainingBuff
from .player_room_state import PlayerRoomState


class PlayerBuildingTraining(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    buff: PlayerBuildingTrainingBuff
    state: PlayerRoomState
    lastUpdateTime: int
    trainer: PlayerBuildingTrainer
    trainee: PlayerBuildingTrainee
    completeWorkTime: DateTime | None = None
