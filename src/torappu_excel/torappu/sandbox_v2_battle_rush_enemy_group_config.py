from pydantic import BaseModel, ConfigDict

from .sandbox_v2_battle_rush_enemy_config import SandboxV2BattleRushEnemyConfig


class SandboxV2BattleRushEnemyGroupConfig(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    enemyGroupKey: str
    enemy: list[SandboxV2BattleRushEnemyConfig]
    dynamicEnemy: list[str]
