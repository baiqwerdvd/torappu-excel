from pydantic import BaseModel, ConfigDict


class ActivityEnemyDuelPoolData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    enemyId: str
    poolNormal: float
    poolSmallEnemy: float
    poolBoss: float
    poolMusic: float
    poolNoSurpriseEnemy: float
