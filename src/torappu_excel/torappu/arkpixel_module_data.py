from .arkpixel_const_data import ArkpixelConstData
from .arkpixel_release_stage_data import ArkpixelReleaseStageData
from ..common import BaseStruct


class ArkpixelModuleData(BaseStruct):
    pixelConstData: ArkpixelConstData
    releaseStageData: dict[str, ArkpixelReleaseStageData]
