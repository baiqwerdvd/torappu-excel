from msgspec import field

from ..common import BaseStruct


class ArkdexCreatureData(BaseStruct):
    creatureNumId: int
    enemyId: str
    deployedEnemyId: str
    trapId: str
    uiDisplayScale: float
    followScale: float
    animSpeedFollow: float
    rarity: int
    specialRarity: bool
    sortId: int
    orderId: str
    name: str
    creatureIcon: str
    worldEntityId: str
    alterNumId: int
    upWeightTagIsShow: bool
    advantageType: str
    description: str
    abilities: list[str]
    obtainApproach: str
    hp: float
    atk: float
    def_: float = field(name="def")
    mag: float
    moveSpeed: float
    atkSpeed: float
    hpPct: int
    atkPct: int
    defPct: int
    magPct: int
    moveSpeedPct: int
    atkSpeedPct: int
