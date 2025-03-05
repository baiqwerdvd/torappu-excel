from .voice_lang_type import VoiceLangType
from ..common import BaseStruct

from msgspec import field


class VoiceLangInfoData(BaseStruct):
    wordkey: str
    voiceLangType: VoiceLangType
    cvName: list[str]
    voicePath: str | None = field(default=None)
