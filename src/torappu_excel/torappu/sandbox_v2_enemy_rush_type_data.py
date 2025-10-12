from pydantic import BaseModel, ConfigDict

from .sandbox_v2_enemy_rush_type import SandboxV2EnemyRushType


class SandboxV2EnemyRushTypeData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    type: SandboxV2EnemyRushType
    description: str
    sortId: int
