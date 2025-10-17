from .player_squad_tmpl import PlayerSquadTmpl
from ..common import BaseStruct


class PlayerSquadItem(BaseStruct):
    charInstId: int
    currentEquip: str | None
    skillIndex: int
    currentTmpl: str | None = None
    tmpl: dict[str, PlayerSquadTmpl] | None = None
