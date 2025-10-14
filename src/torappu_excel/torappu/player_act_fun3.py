from pydantic import BaseModel, ConfigDict

from .player_act_fun_stage import PlayerActFunStage


class PlayerActFun3(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    stages: dict[str, PlayerActFunStage]
