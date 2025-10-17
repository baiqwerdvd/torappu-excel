from msgspec import field

from .grid_position import GridPosition
from .obscured_rect import ObscuredRect
from .shared_consts import SharedConsts
from ..common import BaseStruct


class RangeData(BaseStruct):
    id: str
    direction: SharedConsts.Direction
    grids: list[GridPosition]
    boundingBoxes: list[ObscuredRect] | None = field(default=None)
