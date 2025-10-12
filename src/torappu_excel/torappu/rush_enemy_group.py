from pydantic import BaseModel, ConfigDict

from .rush_enemy_group_config import RushEnemyGroupConfig
from .sandbox_enemy_rush_type import SandboxEnemyRushType


class RushEnemyGroup(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    rushEnemyGroupConfigs: dict[SandboxEnemyRushType, list[RushEnemyGroupConfig]]
    rushEnemyDbRef: list["RushEnemyGroup.RushEnemyDBRef"]

    class RushEnemyDBRef(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        id: str
        level: int
