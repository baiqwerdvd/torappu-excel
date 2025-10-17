from .player_squad_tmpl import PlayerSquadTmpl
from ..common import BaseStruct


class PlayerFriendAssist(BaseStruct):
    charInstId: int
    skillIndex: int
    currentEquip: str
    tmpl: dict[str, PlayerSquadTmpl] | None = None
    currentTmpl: str | None = None
