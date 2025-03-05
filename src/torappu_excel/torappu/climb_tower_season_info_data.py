from ..common import BaseStruct

from msgspec import field


class ClimbTowerSeasonInfoData(BaseStruct):
    id_: str = field(name="id")
    name: str
    seasonNum: int
    startTs: int
    endTs: int
    towers: list[str]
    seasonCards: list[str]
    replicatedTowers: list[str]
    seasonColor: str | None = field(default=None)
