from .sandbox_v2_enemy_rush_type import SandboxV2EnemyRushType
from ..common import BaseStruct

from msgspec import field


class SandboxV2EnemyRushTypeData(BaseStruct):
    type_: SandboxV2EnemyRushType = field(name="type")
    description: str
    sortId: int
