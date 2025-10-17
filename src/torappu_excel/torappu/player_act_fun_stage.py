from .player_stage_state import PlayerStageState
from ..common import BaseStruct


class PlayerActFunStage(BaseStruct):
    state: PlayerStageState
    scores: list[int]
