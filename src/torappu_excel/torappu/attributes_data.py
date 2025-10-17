from msgspec import field

from ..common import BaseStruct


class AttributesData(BaseStruct):
    maxHp: int
    atk: int
    def_: int = field(name="def")
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
    palsyImmune: bool | None = field(default=None)
    disarmedCombatImmune: bool | None = field(default=None)
    fearedImmune: bool | None = field(default=None)
