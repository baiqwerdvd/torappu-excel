from enum import StrEnum

from .enemy_handbook_damage_type import EnemyHandBookDamageType
from .enemy_level_type import EnemyLevelType
from ..common import BaseStruct

from msgspec import field


class EnemyHandBookData(BaseStruct):
    class TextFormat(StrEnum):
        NORMAL = "NORMAL"
        TITLE = "TITLE"
        SILENCE = "SILENCE"

    enemyId: str
    enemyIndex: str
    enemyTags: list[str] | None
    sortId: int
    name: str
    enemyLevel: EnemyLevelType
    description: str
    attackType: str | None
    ability: str | None
    isInvalidKilled: bool
    overrideKillCntInfos: dict[str, int]
    hideInHandbook: bool
    abilityList: list["EnemyHandBookData.Abilty"] | None
    linkEnemies: list[str] | None
    damageType: list[EnemyHandBookDamageType] | None
    invisibleDetail: bool
    hideInStage: bool | None = field(default=None)

    class Abilty(BaseStruct):
        text: str
        textFormat: "EnemyHandBookData.TextFormat"
