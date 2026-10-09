from .arkvent_audio_meta_flag import ArkventAudioMetaFlag
from .arkvent_audio_roll_off_type import ArkventAudioRollOffType
from .arkvent_audio_spatial_profile import ArkventAudioSpatialProfile
from .arkvent_audio_trigger_mode import ArkventAudioTriggerMode
from .arkvent_range_data import ArkventRangeData
from ..common import BaseStruct


class ArkventAudioSourceData(BaseStruct):
    id: str
    positionX: float
    positionY: float
    positionZ: float
    module: str
    signal: str
    subSignal: str
    meta: ArkventAudioMetaFlag
    soundPlaybackPolicy: int
    minDist: float
    maxDist: float
    rollOffType: ArkventAudioRollOffType
    spatialBlend: ArkventAudioSpatialProfile | None
    spatialVolume: ArkventAudioSpatialProfile | None
    volume: float
    effectiveRange: ArkventRangeData
    triggerMode: ArkventAudioTriggerMode
    periodicFixedInterval: float
    periodicMinInterval: float
    periodicMaxInterval: float
    applyIntervalOnFirstPlay: bool
    fadeOutTime: float
    mutexGroup: str
    mutexOrder: int
    bindActors: list[str] | None
    tags: list[str] | None
