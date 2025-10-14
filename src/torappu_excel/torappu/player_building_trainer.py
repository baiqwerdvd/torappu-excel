from pydantic import BaseModel, ConfigDict

from .player_building_trainer_state import PlayerBuildingTrainerState


class PlayerBuildingTrainer(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    state: PlayerBuildingTrainerState
    charInstId: int
