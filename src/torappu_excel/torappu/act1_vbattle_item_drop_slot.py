from .act1_vweighted_battle_item_pool import Act1VWeightedBattleItemPool
from ..common import BaseStruct


class Act1VBattleItemDropSlot(BaseStruct):
    prob: float
    itemPools: list[Act1VWeightedBattleItemPool]
