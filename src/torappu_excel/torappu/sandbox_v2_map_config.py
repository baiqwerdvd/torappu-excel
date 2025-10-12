from pydantic import BaseModel, ConfigDict

from .vector2 import Vector2


class SandboxV2MapConfig(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    isRift: bool
    isGuide: bool
    cameraBoundMin: Vector2
    cameraBoundMax: Vector2
    cameraMaxNormalizedZoom: float
    backgroundId: str
