from msgspec import field

from .voice_lang_info_data import VoiceLangInfoData
from .voice_lang_type import VoiceLangType
from ..common import BaseStruct


class VoiceLangData(BaseStruct):
    wordkeys: list[str]
    charId: str
    dict_: dict[VoiceLangType, VoiceLangInfoData] = field(name="dict")
