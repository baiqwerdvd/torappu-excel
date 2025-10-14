from pydantic import BaseModel, ConfigDict

from .player_training_camp_stage import PlayerTrainingCampStage


class PlayerTrainingCamp(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    stages: dict[str, PlayerTrainingCampStage]
