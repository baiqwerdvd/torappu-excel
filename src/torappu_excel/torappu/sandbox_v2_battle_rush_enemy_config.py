from pydantic import BaseModel, ConfigDict


class SandboxV2BattleRushEnemyConfig(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    enemyKey: str
    branchId: str
    count: int
    interval: float
    preDelay: float
