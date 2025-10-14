from pydantic import BaseModel, ConfigDict

from .building_buff_display import BuildingBuffDisplay
from .player_building_manufacture_buff import PlayerBuildingManufactureBuff
from .player_room_state import PlayerRoomState


class PlayerBuildingManufacture(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    buff: PlayerBuildingManufactureBuff
    state: PlayerRoomState
    formulaId: str
    remainSolutionCnt: int
    outputSolutionCnt: int
    lastUpdateTime: int
    processPoint: float
    saveTime: int
    completeWorkTime: int
    capacity: int
    apCost: int
    display: BuildingBuffDisplay
    tailTime: float | int
    presetQueue: list[list[int]]
