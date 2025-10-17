from msgspec import field

from ..common import BaseStruct


class ClimbTowerSeasonInfoData(BaseStruct):
    id: str
    name: str
    seasonNum: int
    startTs: int
    endTs: int
    towers: list[str]
    seasonCards: list[str]
    replicatedTowers: list[str]
    seasonColor: str | None = field(default=None)
