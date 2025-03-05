from ..common import BaseStruct


class RoguelikeDiceData(BaseStruct):
    diceId: str
    description: str
    isUpgradeDice: int
    upgradeDiceId: str | None
    diceFaceCount: int
    battleDiceId: str
