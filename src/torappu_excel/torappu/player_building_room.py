from typing import Any

from msgspec import field

from .player_building_control import PlayerBuildingControl
from .player_building_dormitory import PlayerBuildingDormitory
from .player_building_hire import PlayerBuildingHire
from .player_building_manufacture import PlayerBuildingManufacture
from .player_building_meeting import PlayerBuildingMeeting
from .player_building_power import PlayerBuildingPower
from .player_building_private import PlayerBuildingPrivate
from .player_building_shop import PlayerBuildingShop
from .player_building_trading import PlayerBuildingTrading
from .player_building_training import PlayerBuildingTraining
from .player_building_workshop import PlayerBuildingWorkshop
from ..common import BaseStruct


class PlayerBuildingRoom(BaseStruct):
    MANUFACTURE: dict[str, PlayerBuildingManufacture] = field(default_factory=dict)
    POWER: dict[str, PlayerBuildingPower] = field(default_factory=dict)
    CONTROL: dict[str, PlayerBuildingControl] = field(default_factory=dict)
    MEETING: dict[str, PlayerBuildingMeeting] = field(default_factory=dict)
    HIRE: dict[str, PlayerBuildingHire] = field(default_factory=dict)
    DORMITORY: dict[str, PlayerBuildingDormitory] = field(default_factory=dict)
    PRIVATE: dict[str, PlayerBuildingPrivate] = field(default_factory=dict)
    TRAINING: dict[str, PlayerBuildingTraining] = field(default_factory=dict)
    WORKSHOP: dict[str, PlayerBuildingWorkshop] = field(default_factory=dict)
    TRADING: dict[str, PlayerBuildingTrading] = field(default_factory=dict)
    CORRIDOR: dict[str, dict[str, Any]] = field(default_factory=dict)
    ELEVATOR: dict[str, dict[str, Any]] = field(default_factory=dict)
    SHOP: dict[str, PlayerBuildingShop] | None = None
