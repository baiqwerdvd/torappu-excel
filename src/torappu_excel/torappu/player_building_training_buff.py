from pydantic import BaseModel, ConfigDict

from .player_building_training_reduce_time_bd import PlayerBuildingTrainingReduceTimeBd


class PlayerBuildingTrainingBuff(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    speed: float
    apCost: int
    lvEx: dict[str, float | int]
    lvCost: dict[str, int]
    reduce: "PlayerBuildingTrainingBuff.Reduce"
    reduceTimeBd: PlayerBuildingTrainingReduceTimeBd

    class Reduce(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        target: int | None
        progress: int
        cut: float | int
