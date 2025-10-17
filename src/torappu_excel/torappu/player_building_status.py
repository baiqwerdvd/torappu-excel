from .player_building_labor import PlayerBuildingLabor
from .player_building_workshop_status import PlayerBuildingWorkshopStatus
from ..common import BaseStruct


class PlayerBuildingStatus(BaseStruct):
    labor: PlayerBuildingLabor
    workshop: PlayerBuildingWorkshopStatus
