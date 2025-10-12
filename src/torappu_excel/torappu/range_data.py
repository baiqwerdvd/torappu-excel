from pydantic import BaseModel, ConfigDict, Field

from .grid_position import GridPosition
from .obscured_rect import ObscuredRect
from .shared_consts import SharedConsts


class RangeData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    direction: SharedConsts.Direction
    grids: list[GridPosition]
    boundingBoxes: list[ObscuredRect] | None = Field(default=None)
