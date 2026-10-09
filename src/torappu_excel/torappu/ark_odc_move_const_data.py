from .arkvent_move_preset_data import ArkventMovePresetData
from .spine_flip_mode import SpineFlipMode
from ..common import BaseStruct


class ArkOdcMoveConstData(BaseStruct):
    runMaxStableMoveSpeed: float
    walkMaxStableMoveSpeed: float
    stableMovementSharpness: float
    defaultAlpha: float
    runConfiguredAnimScale: float
    walkConfiguredAnimScale: float
    minAnimScale: float
    maxAnimScale: float
    spineFlip: SpineFlipMode
    defaultSlideStopThreshold: float
    presetData: ArkventMovePresetData
