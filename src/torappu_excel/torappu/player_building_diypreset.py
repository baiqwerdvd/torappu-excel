from pydantic import BaseModel, ConfigDict

from .player_building_diysolution import PlayerBuildingDIYSolution


class PlayerBuildingDIYPreset(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    name: str
    roomType: str
    solution: PlayerBuildingDIYSolution
    thumbnail: str
