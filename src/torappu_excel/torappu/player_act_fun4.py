from pydantic import BaseModel, ConfigDict

from .player_act_fun4_mission import PlayerActFun4Mission
from .player_act_fun4_stage import PlayerActFun4Stage


class PlayerActFun4(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    stages: dict[str, PlayerActFun4Stage]
    liveEndings: dict[str, int]
    cameraLv: int
    fans: int
    posts: int
    missions: dict[str, PlayerActFun4Mission]
