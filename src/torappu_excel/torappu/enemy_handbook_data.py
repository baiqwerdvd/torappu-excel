from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field

from .enemy_handbook_damage_type import EnemyHandBookDamageType
from .enemy_level_type import EnemyLevelType


class EnemyHandBookData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

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
    hideInStage: bool | None = Field(default=None)

    class Abilty(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        text: str
        textFormat: "EnemyHandBookData.TextFormat"
