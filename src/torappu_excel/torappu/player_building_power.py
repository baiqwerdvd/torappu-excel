from pydantic import BaseModel, ConfigDict

from .player_building_power_buff import PlayerBuildingPowerBuff


class PlayerBuildingPower(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    buff: PlayerBuildingPowerBuff
    presetQueue: list[list[int]]
