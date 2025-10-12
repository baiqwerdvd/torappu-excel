from pydantic import BaseModel, ConfigDict

from .enemy_duel_bet_strategy import EnemyDuelBetStrategy


class ActivityEnemyDuelNpcData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    npcId: str
    avatarId: str
    name: str
    priority: float
    specialStrategy: EnemyDuelBetStrategy
    npcProb: float
    defaultEnemyScore: float
    allinProb: float
