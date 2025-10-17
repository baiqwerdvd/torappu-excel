from msgspec import field

from .voice_lang_type import VoiceLangType
from ..common import BaseStruct


class VoiceLangInfoData(BaseStruct):
    wordkey: str
    voiceLangType: VoiceLangType
    cvName: list[str]
    voicePath: str | None = field(default=None)
