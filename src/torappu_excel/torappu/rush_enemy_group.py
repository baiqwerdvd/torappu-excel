from .rush_enemy_group_config import RushEnemyGroupConfig
from .sandbox_enemy_rush_type import SandboxEnemyRushType
from ..common import BaseStruct

from msgspec import field


class RushEnemyGroup(BaseStruct):
    rushEnemyGroupConfigs: dict[SandboxEnemyRushType, list[RushEnemyGroupConfig]]
    rushEnemyDbRef: list["RushEnemyGroup.RushEnemyDBRef"]

    class RushEnemyDBRef(BaseStruct):
        id_: str = field(name="id")
        level: int
