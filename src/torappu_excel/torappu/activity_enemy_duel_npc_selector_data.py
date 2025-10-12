from pydantic import BaseModel, ConfigDict


class ActivityEnemyDuelNpcSelectorData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    enemyId: str
    score: float
