from pydantic import BaseModel, ConfigDict

from .player_building_trainee_state import PlayerBuildingTraineeState


class PlayerBuildingTrainee(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    state: PlayerBuildingTraineeState
    charInstId: int
    processPoint: float
    speed: float
    targetSkill: int
