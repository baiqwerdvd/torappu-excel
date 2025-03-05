from .vector2 import Vector2
from ..common import BaseStruct


class SandboxV2MapConfig(BaseStruct):
    isRift: bool
    isGuide: bool
    cameraBoundMin: Vector2
    cameraBoundMax: Vector2
    cameraMaxNormalizedZoom: float
    backgroundId: str
