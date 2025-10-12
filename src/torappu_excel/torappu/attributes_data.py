from pydantic import BaseModel, ConfigDict, Field


class AttributesData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    maxHp: int
    atk: int
    def_: int = Field(alias="def")
    magicResistance: float
    cost: int
    blockCnt: int
    moveSpeed: float
    attackSpeed: float
    baseAttackTime: float
    respawnTime: int
    hpRecoveryPerSec: float
    spRecoveryPerSec: float
    maxDeployCount: int
    maxDeckStackCnt: int
    tauntLevel: int
    massLevel: int
    baseForceLevel: int
    stunImmune: bool
    silenceImmune: bool
    sleepImmune: bool
    frozenImmune: bool
    levitateImmune: bool
    attractImmune: bool
    palsyImmune: bool | None = Field(default=None)
    disarmedCombatImmune: bool | None = Field(default=None)
    fearedImmune: bool | None = Field(default=None)
