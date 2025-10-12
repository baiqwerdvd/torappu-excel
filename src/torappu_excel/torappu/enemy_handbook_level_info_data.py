from pydantic import BaseModel, ConfigDict, Field


class EnemyHandbookLevelInfoData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    classLevel: str
    attack: "EnemyHandbookLevelInfoData.RangePair"
    def_: "EnemyHandbookLevelInfoData.RangePair" = Field(alias="def")
    magicRes: "EnemyHandbookLevelInfoData.RangePair"
    maxHP: "EnemyHandbookLevelInfoData.RangePair"
    moveSpeed: "EnemyHandbookLevelInfoData.RangePair"
    attackSpeed: "EnemyHandbookLevelInfoData.RangePair"
    enemyDamageRes: "EnemyHandbookLevelInfoData.RangePair"
    enemyRes: "EnemyHandbookLevelInfoData.RangePair"

    class RangePair(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        min: float
        max: float
