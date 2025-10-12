from pydantic import BaseModel, ConfigDict

from .rush_enemy_config import RushEnemyConfig


class RushEnemyGroupConfig(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    enemyGroupKey: str
    weight: int
    enemy: list[RushEnemyConfig]
    dynamicEnemy: list[str]
