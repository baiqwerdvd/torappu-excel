from .player_squad_tmpl import PlayerSquadTmpl
from ..common import BaseStruct


class PlayerSquadItem(BaseStruct):
    charInstId: int
    skillIndex: int
    currentEquip: str | None = None
    currentTmpl: str | None = None
    tmpl: dict[str, PlayerSquadTmpl] | None = None
