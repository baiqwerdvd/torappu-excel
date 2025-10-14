from pydantic import BaseModel, ConfigDict

from .player_squad_tmpl import PlayerSquadTmpl


class PlayerSquadItem(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    charInstId: int
    currentEquip: str | None
    skillIndex: int
    currentTmpl: str | None = None
    tmpl: dict[str, PlayerSquadTmpl] | None = None
