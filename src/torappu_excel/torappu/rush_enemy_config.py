from pydantic import BaseModel, ConfigDict


class RushEnemyConfig(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    enemyKey: str
    branchId: str
    count: int
    interval: float | int
