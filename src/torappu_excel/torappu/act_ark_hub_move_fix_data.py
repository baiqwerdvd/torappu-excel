from .spine_flip_mode import SpineFlipMode
from ..common import BaseStruct


class ActArkHubMoveFixData(BaseStruct):
    skinId: str
    runMaxStableMoveSpeed: float
    walkMaxStableMoveSpeed: float
    alpha: float
    runConfiguredAnimScale: float
    walkConfiguredAnimScale: float
    slideStopThreshold: float
    spineFlip: SpineFlipMode
