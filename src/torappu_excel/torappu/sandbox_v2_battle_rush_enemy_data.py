from pydantic import BaseModel, ConfigDict

from .sandbox_v2_battle_rush_enemy_group_config import SandboxV2BattleRushEnemyGroupConfig
from .sandbox_v2_enemy_rush_type import SandboxV2EnemyRushType


class SandboxV2BattleRushEnemyData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    rushEnemyGroupConfigs: dict[SandboxV2EnemyRushType, list[SandboxV2BattleRushEnemyGroupConfig]]
    rushEnemyDbRef: list["SandboxV2BattleRushEnemyData.RushEnemyDBRef"]

    class RushEnemyDBRef(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        id: str
        level: int
