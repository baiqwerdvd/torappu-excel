from .player_squad_item import PlayerSquadItem
from ..common import BaseStruct


class PlayerSquad(BaseStruct):
    squadId: str
    name: str
    slots: list[PlayerSquadItem | None]
