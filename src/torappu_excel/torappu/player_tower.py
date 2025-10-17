from .tower_current import TowerCurrent
from .tower_outer import TowerOuter
from .tower_season import TowerSeason
from ..common import BaseStruct


class PlayerTower(BaseStruct):
    current: TowerCurrent
    outer: TowerOuter
    season: TowerSeason
