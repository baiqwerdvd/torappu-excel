from .player_roguelike_cursor import PlayerRoguelikeCursor
from ..common import BaseStruct


class PlayerRoguelikeStatus(BaseStruct):
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
