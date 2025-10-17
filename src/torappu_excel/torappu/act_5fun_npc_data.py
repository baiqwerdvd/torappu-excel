from .npc_strategy import NpcStrategy
from ..common import BaseStruct


class Act5FunNpcData(BaseStruct):
    npcId: str
    avatarId: str
    name: str
    priority: float | int
    specialStrategy: NpcStrategy
    npcProb: float | int
    defaultEnemyScore: float | int
