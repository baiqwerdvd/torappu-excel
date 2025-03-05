from ..common import BaseStruct

from msgspec import field


class EnemyHandbookLevelInfoData(BaseStruct):
    classLevel: str
    attack: "EnemyHandbookLevelInfoData.RangePair"
    def_: "EnemyHandbookLevelInfoData.RangePair" = field(name="def")
    magicRes: "EnemyHandbookLevelInfoData.RangePair"
    maxHP: "EnemyHandbookLevelInfoData.RangePair"
    moveSpeed: "EnemyHandbookLevelInfoData.RangePair"
    attackSpeed: "EnemyHandbookLevelInfoData.RangePair"
    enemyDamageRes: "EnemyHandbookLevelInfoData.RangePair"
    enemyRes: "EnemyHandbookLevelInfoData.RangePair"

    class RangePair(BaseStruct):
        min_: float = field(name="min")
        max_: float = field(name="max")
