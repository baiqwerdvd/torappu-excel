from pydantic import BaseModel, ConfigDict

from .player_roguelike_cursor import PlayerRoguelikeCursor


class PlayerRoguelikeStatus(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    uuid: str
    level: int
    exp: int
    hp: int
    gold: int
    squadCapacity: int
    populationCost: int
    populationMax: int
    cursor: PlayerRoguelikeCursor
    perfectWinStreak: int
    mode: str
    ending: str
    showBattleCharInstId: int
    startTime: int
    endTime: int
