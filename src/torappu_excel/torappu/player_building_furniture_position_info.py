from pydantic import BaseModel, ConfigDict

from .player_building_grid_position import PlayerBuildingGridPosition


class PlayerBuildingFurniturePositionInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    coordinate: PlayerBuildingGridPosition
