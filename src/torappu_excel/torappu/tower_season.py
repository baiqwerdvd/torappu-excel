from pydantic import BaseModel, ConfigDict

from .player_squad_item import PlayerSquadItem


class TowerSeason(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    finishTs: int
    missions: dict[str, "TowerSeason.TowerSeasonMission"]
    passWithGodCard: dict[str, list[str]]
    slots: dict[str, "list[TowerSeason.TowerSeasonCardSquad]"]
    period: "TowerSeason.TowerSeasonPeriod"

    class TowerSeasonMission(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        target: int
        value: int
        hasRecv: bool

    class TowerSeasonCardSquad(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        godCardId: str
        squad: list[PlayerSquadItem]

    class TowerSeasonPeriod(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        termTs: int
        items: dict[str, int]
        cur: int
        len: int
