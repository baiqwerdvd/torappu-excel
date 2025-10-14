from pydantic import BaseModel, ConfigDict

from .player_building_hire_buff import PlayerBuildingHireBuff
from .player_building_hiring_state import PlayerBuildingHiringState


class PlayerBuildingHire(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    buff: PlayerBuildingHireBuff
    recruitSlotId: int | None = None
    state: PlayerBuildingHiringState
    processPoint: float
    speed: float
    lastUpdateTime: int
    refreshCount: int
    completeWorkTime: int
    presetQueue: list[list[int]]
