from pydantic import BaseModel, ConfigDict

from .player_squad_item import PlayerSquadItem


class PlayerSquad(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    squadId: int
    name: str
    slots: list[PlayerSquadItem | None]
