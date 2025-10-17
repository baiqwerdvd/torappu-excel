from .voice_lang_type import VoiceLangType
from ..common import BaseStruct


class VoiceLangGroupData(BaseStruct):
    name: str
    members: list[VoiceLangType]
