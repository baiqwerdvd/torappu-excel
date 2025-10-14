from pydantic import BaseModel, ConfigDict

from .player_building_labor import PlayerBuildingLabor
from .player_building_workshop_status import PlayerBuildingWorkshopStatus


class PlayerBuildingStatus(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    labor: PlayerBuildingLabor
    workshop: PlayerBuildingWorkshopStatus
