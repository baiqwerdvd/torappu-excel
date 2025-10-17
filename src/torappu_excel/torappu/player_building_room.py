from typing import Any

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
    MANUFACTURE: dict[str, PlayerBuildingManufacture]
    POWER: dict[str, PlayerBuildingPower]
    CONTROL: dict[str, PlayerBuildingControl]
    MEETING: dict[str, PlayerBuildingMeeting]
    HIRE: dict[str, PlayerBuildingHire]
    DORMITORY: dict[str, PlayerBuildingDormitory]
    PRIVATE: dict[str, PlayerBuildingPrivate]
    TRAINING: dict[str, PlayerBuildingTraining]
    WORKSHOP: dict[str, PlayerBuildingWorkshop]
    TRADING: dict[str, PlayerBuildingTrading]
    CORRIDOR: dict[str, dict[str, Any]]
    ELEVATOR: dict[str, dict[str, Any]]
    SHOP: dict[str, PlayerBuildingShop] | None = None
