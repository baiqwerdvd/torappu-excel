from .arkvent_audio_spatial_type import ArkventAudioSpatialType
from ..common import BaseStruct


class ArkventAudioSpatialProfile(BaseStruct):
    type: ArkventAudioSpatialType
    name: str
