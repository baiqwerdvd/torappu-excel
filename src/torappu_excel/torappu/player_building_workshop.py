from .player_building_workshop_buff import PlayerBuildingWorkshopBuff
from ..common import BaseStruct


class PlayerBuildingWorkshop(BaseStruct):
    buff: PlayerBuildingWorkshopBuff
    statistic: "PlayerBuildingWorkshop.Statistic"

    class Statistic(BaseStruct):
        noAddition: int
