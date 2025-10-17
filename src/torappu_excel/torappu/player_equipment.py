from .player_equip_mission import PlayerEquipMission
from ..common import BaseStruct


class PlayerEquipment(BaseStruct):
    missions: dict[str, PlayerEquipMission]
