from .player_building_diysolution import PlayerBuildingDIYSolution
from ..common import BaseStruct


class PlayerBuildingDormitory(BaseStruct):
    buff: "PlayerBuildingDormitory.Buff"
    comfort: int
    diySolution: PlayerBuildingDIYSolution
    lockQueue: list[int]

    class Buff(BaseStruct):
        apCost: "PlayerBuildingDormitory.Buff.APCost"
        point: dict[str, int]

        class APCost(BaseStruct):
            all: int
            self: dict[str, float | int]
            single: "PlayerBuildingDormitory.Buff.APCost.SingleTarget"
            exclude: dict[str, int]

            class SingleTarget(BaseStruct):
                target: str | None
                value: int
