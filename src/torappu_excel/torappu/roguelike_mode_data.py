from ..common import BaseStruct


class RoguelikeModeData(BaseStruct):
    id: str
    name: str
    canUnlockItem: int
    scoreFactor: float
    itemPools: list[str]
    difficultyDesc: str
    ruleDesc: str
    sortId: int
    unlockMode: str
    color: str
