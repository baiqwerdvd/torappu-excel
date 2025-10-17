from .player_act_fun6_stage import PlayerActFun6Stage
from ..common import BaseStruct


class PlayerActFun6(BaseStruct):
    stages: dict[str, PlayerActFun6Stage]
    recvList: list[str]
