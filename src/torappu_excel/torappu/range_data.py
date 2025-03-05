from .grid_position import GridPosition
from .obscured_rect import ObscuredRect
from .shared_consts import SharedConsts
from ..common import BaseStruct

from msgspec import field


class RangeData(BaseStruct):
    id_: str = field(name="id")
    direction: SharedConsts.Direction
    grids: list[GridPosition]
    boundingBoxes: list[ObscuredRect] | None = field(default=None)
