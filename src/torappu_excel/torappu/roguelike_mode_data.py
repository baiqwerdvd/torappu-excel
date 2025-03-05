from ..common import BaseStruct

from msgspec import field


class RoguelikeModeData(BaseStruct):
    id_: str = field(name="id")
    name: str
    canUnlockItem: int
    scoreFactor: float
    itemPools: list[str]
    difficultyDesc: str
    ruleDesc: str
    sortId: int
    unlockMode: str
    color: str
