from pydantic import BaseModel, ConfigDict, Field

from .vector2 import Vector2


class SandboxV2MapZoneData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    zoneId: str
    hasBorder: bool
    center: Vector2 | None = Field(default=None)
    vertices: list[Vector2] | None = Field(default=None)
    triangles: list[list[int]] | None = Field(default=None)
