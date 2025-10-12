from pydantic import BaseModel, ConfigDict

from .vector2 import Vector2


class SpecialOperatorPointPosData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    pos: Vector2
