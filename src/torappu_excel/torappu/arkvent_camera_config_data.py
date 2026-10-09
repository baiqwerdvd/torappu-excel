from .arkvent_camera_platform_config import ArkventCameraPlatformConfig
from ..common import BaseStruct


class ArkventCameraConfigData(BaseStruct):
    pcConfig: ArkventCameraPlatformConfig
    mobileConfig: ArkventCameraPlatformConfig | None
