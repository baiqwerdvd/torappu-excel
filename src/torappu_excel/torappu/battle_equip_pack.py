from .battle_equip_per_level_pack import BattleEquipPerLevelPack
from ..common import BaseStruct


class BattleEquipPack(BaseStruct):
    phases: list[BattleEquipPerLevelPack]
