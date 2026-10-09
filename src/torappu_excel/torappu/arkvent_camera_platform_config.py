from .arkvent_camera_blend_style import ArkventCameraBlendStyle
from .vector3 import Vector3
from ..common import BaseStruct


class ArkventCameraPlatformConfig(BaseStruct):
    blendDuration: float
    blendStyle: ArkventCameraBlendStyle
    pitch: float
    cameraDistance: float
    lookAheadTime: float
    lookAheadSmoothing: float
    screenX: float
    screenY: float
    trackedObjectOffset: Vector3
    deadZoneWidth: float
    deadZoneHeight: float
    deadZoneDepth: float
    softZoneWidth: float
    softZoneHeight: float
    biasX: float
    biasY: float
    xDamping: float
    yDamping: float
    zDamping: float
