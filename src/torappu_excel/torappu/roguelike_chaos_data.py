from ..common import BaseStruct


class RoguelikeChaosData(BaseStruct):
    chaosId: str
    level: int
    nextChaosId: str | None
    prevChaosId: str | None
    iconId: str
    name: str
    functionDesc: str
    desc: str
    sound: str
    sortId: int
