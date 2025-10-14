from pydantic import BaseModel, ConfigDict

from .tower_current import TowerCurrent
from .tower_outer import TowerOuter
from .tower_season import TowerSeason


class PlayerTower(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    current: TowerCurrent
    outer: TowerOuter
    season: TowerSeason
