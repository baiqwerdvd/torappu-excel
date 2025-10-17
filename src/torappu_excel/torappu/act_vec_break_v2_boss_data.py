from ..common import BaseStruct


class ActVecBreakV2BossData(BaseStruct):
    enemyId: str
    name: str
    desc: str | None
    level: int
    iconId: str
    levelDecoFigureId: str | None
    levelDecoSignId: str | None
    decoId: str | None
