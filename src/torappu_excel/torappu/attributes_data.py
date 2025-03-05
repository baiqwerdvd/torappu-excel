from ..common import BaseStruct

from msgspec import field


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
    disarmedCombatImmune: bool = False
    fearedImmune: bool = False
