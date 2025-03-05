from .battle_uni_equip_data import BattleUniEquipData
from .blackboard import Blackboard
from ..common import BaseStruct


class BattleEquipPerLevelPack(BaseStruct):
    equipLevel: int
    parts: list[BattleUniEquipData]
    attributeBlackboard: list[Blackboard]
    tokenAttributeBlackboard: dict[str, list[Blackboard]]
