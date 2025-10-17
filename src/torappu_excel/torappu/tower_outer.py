from .player_squad_item import PlayerSquadItem
from .tower_game_strategy import TowerGameStrategy
from .tower_tactical import TowerTactical
from ..common import BaseStruct


class TowerOuter(BaseStruct):
    training: dict[str, int]
    towers: dict[str, "TowerOuter.TowerData"]
    hasTowerPass: int
    pickedGodCard: dict[str, list[str]]
    tactical: TowerTactical
    strategy: TowerGameStrategy
    squad: list[PlayerSquadItem] | None = None

    class TowerData(BaseStruct):
        best: int
        reward: list[int]
        unlockHard: bool
        hardBest: int
        canSweep: bool | None = None
        canSweepHard: bool | None = None
