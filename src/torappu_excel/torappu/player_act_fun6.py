from pydantic import BaseModel, ConfigDict

from .player_act_fun6_stage import PlayerActFun6Stage


class PlayerActFun6(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    stages: dict[str, PlayerActFun6Stage]
    recvList: list[str]
