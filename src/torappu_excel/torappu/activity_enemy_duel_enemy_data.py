from pydantic import BaseModel, ConfigDict


class ActivityEnemyDuelEnemyData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    enemyId: str
    originalEnemyId: str
