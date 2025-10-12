from pydantic import BaseModel, ConfigDict


class Act1VHalfIdleEnemyPreloadMeta(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    enemyId: str
    level: int
