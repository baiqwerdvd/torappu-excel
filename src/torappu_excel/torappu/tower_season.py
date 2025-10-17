from .player_squad_item import PlayerSquadItem
from ..common import BaseStruct


class TowerSeason(BaseStruct):
    id: str
    finishTs: int
    missions: dict[str, "TowerSeason.TowerSeasonMission"]
    passWithGodCard: dict[str, list[str]]
    slots: dict[str, "list[TowerSeason.TowerSeasonCardSquad]"]
    period: "TowerSeason.TowerSeasonPeriod"

    class TowerSeasonMission(BaseStruct):
        target: int
        value: int
        hasRecv: bool

    class TowerSeasonCardSquad(BaseStruct):
        godCardId: str
        squad: list[PlayerSquadItem]

    class TowerSeasonPeriod(BaseStruct):
        termTs: int
        items: dict[str, int]
        cur: int
        len: int
