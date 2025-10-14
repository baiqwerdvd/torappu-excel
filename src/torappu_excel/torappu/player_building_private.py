from pydantic import BaseModel, ConfigDict

from .player_building_diysolution import PlayerBuildingDIYSolution


class PlayerBuildingPrivate(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    owners: list[int]
    comfort: int
    diySolution: PlayerBuildingDIYSolution
