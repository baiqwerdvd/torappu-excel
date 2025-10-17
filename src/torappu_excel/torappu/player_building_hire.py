from .player_building_hire_buff import PlayerBuildingHireBuff
from .player_building_hiring_state import PlayerBuildingHiringState
from ..common import BaseStruct


class PlayerBuildingHire(BaseStruct):
    buff: PlayerBuildingHireBuff
    state: PlayerBuildingHiringState
    processPoint: float
    speed: float
    lastUpdateTime: int
    refreshCount: int
    completeWorkTime: int
    presetQueue: list[list[int]]
    recruitSlotId: int | None = None
