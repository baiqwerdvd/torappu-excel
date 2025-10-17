from .player_act_fun4_mission import PlayerActFun4Mission
from .player_act_fun4_stage import PlayerActFun4Stage
from ..common import BaseStruct


class PlayerActFun4(BaseStruct):
    stages: dict[str, PlayerActFun4Stage]
    liveEndings: dict[str, int]
    cameraLv: int
    fans: int
    posts: int
    missions: dict[str, PlayerActFun4Mission]
