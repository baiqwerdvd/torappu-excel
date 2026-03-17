from .player_stage_state import PlayerStageState
from ..common import BaseStruct


class PlayerActFun7(BaseStruct):
    stages: dict[str, PlayerStageState]
