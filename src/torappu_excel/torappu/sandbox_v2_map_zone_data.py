from msgspec import field

from .vector2 import Vector2
from ..common import BaseStruct


class SandboxV2MapZoneData(BaseStruct):
    zoneId: str
    hasBorder: bool
    center: Vector2 | None = field(default=None)
    vertices: list[Vector2] | None = field(default=None)
    triangles: list[list[int]] | None = field(default=None)
