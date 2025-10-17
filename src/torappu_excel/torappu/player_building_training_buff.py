from .player_building_training_reduce_time_bd import PlayerBuildingTrainingReduceTimeBd
from ..common import BaseStruct


class PlayerBuildingTrainingBuff(BaseStruct):
    speed: float
    apCost: int
    lvEx: dict[str, float | int]
    lvCost: dict[str, int]
    reduce: "PlayerBuildingTrainingBuff.Reduce"
    reduceTimeBd: PlayerBuildingTrainingReduceTimeBd

    class Reduce(BaseStruct):
        target: int | None
        progress: int
        cut: float | int
