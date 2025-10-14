from pydantic import BaseModel, ConfigDict

from .player_squad_tmpl import PlayerSquadTmpl


class PlayerFriendAssist(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    charInstId: int
    currentTmpl: str | None = None
    skillIndex: int
    currentEquip: str
    tmpl: dict[str, PlayerSquadTmpl] | None = None
