from .activity_enemy_duel_npc_selector_data import ActivityEnemyDuelNpcSelectorData
from ..common import BaseStruct


class ActivityEnemyDuelNpcSelectorGroupData(BaseStruct):
    npcId: str
    data: list[ActivityEnemyDuelNpcSelectorData]
