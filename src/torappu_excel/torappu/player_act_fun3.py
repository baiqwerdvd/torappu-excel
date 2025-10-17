from .player_act_fun_stage import PlayerActFunStage
from ..common import BaseStruct


class PlayerActFun3(BaseStruct):
    stages: dict[str, PlayerActFunStage]
