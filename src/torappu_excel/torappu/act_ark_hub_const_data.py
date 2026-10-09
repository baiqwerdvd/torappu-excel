from .ping_cond import PingCond
from .spine_flip_mode import SpineFlipMode
from ..common import BaseStruct


class ActArkHubConstData(BaseStruct):
    maxChannelPlayerLimit: int
    emojiCD: float
    emojiTime: float
    runMaxStableMoveSpeed: float
    walkMaxStableMoveSpeed: float
    stableMovementSharpness: float
    defaultAlpha: float
    runConfiguredAnimScale: float
    walkConfiguredAnimScale: float
    minAnimScale: float
    maxAnimScale: float
    defaultMovePreset: str
    defaultSpineFlip: SpineFlipMode
    defaultSlideStopThreshold: float
    reportMaxNum: int
    invitationSendCd: int
    invitationValidityPeriod: int
    storyMachineCameraConfigId: str
    pingConds: list[PingCond]
    btnCancelInteractStyleId: str
    npcDefaultFx: str
    npcSelectedFx: str
    enterLobbyFx: str
    interactSelectedFx: str
    spraySummonFx: str
    sprayFadeFx: str
    petSummonFx: str
    followDistance: float
    stopDistance: float
    moveSpeed: float
    followOffset: float
    colorSpineOutline: str
    highQualityPetSpineCount: int
    lowQualityPetSpineCount: int
    midQualityPetSpineCount: int
