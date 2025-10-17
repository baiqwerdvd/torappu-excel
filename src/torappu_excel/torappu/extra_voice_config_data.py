from .voice_lang_type import VoiceLangType
from ..common import BaseStruct


class ExtraVoiceConfigData(BaseStruct):
    voiceId: str
    validVoiceLang: list[VoiceLangType]
