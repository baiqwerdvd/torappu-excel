from .act1_vhalf_idle_battle_item_type import Act1VHalfIdleBattleItemType
from ..common import BaseStruct


class Act1VWeightedBattleItemPool(BaseStruct):
    poolKey: str
    type: Act1VHalfIdleBattleItemType
    weight: float
