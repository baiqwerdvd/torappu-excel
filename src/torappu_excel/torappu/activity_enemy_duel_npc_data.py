from .enemy_duel_bet_strategy import EnemyDuelBetStrategy
from ..common import BaseStruct


class ActivityEnemyDuelNpcData(BaseStruct):
    npcId: str
    avatarId: str
    name: str
    priority: float
    specialStrategy: EnemyDuelBetStrategy
    npcProb: float
    defaultEnemyScore: float
    allinProb: float
