from msgspec import field

from ..common import BaseStruct


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
        min: float
        max: float
