from pydantic import BaseModel, ConfigDict

from .player_building_control_buff import PlayerBuildingControlBuff


class PlayerBuildingControl(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    buff: PlayerBuildingControlBuff
    apCost: int
    lastUpdateTime: int
    presetQueue: list[list[int]]
