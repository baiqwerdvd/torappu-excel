from pydantic import BaseModel, ConfigDict

from .vector2 import Vector2


class SpecialOperatorLinePosData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    startPos: Vector2
    endPos: Vector2
