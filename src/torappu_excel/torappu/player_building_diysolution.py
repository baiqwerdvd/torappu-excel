from pydantic import BaseModel, ConfigDict

from .player_building_furniture_position_info import PlayerBuildingFurniturePositionInfo


class PlayerBuildingDIYSolution(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    wallPaper: str | None
    floor: str | None
    carpet: list[PlayerBuildingFurniturePositionInfo]
    other: list[PlayerBuildingFurniturePositionInfo]
