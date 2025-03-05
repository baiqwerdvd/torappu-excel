from .voice_lang_group_type import VoiceLangGroupType
from ..common import BaseStruct


class VoiceLangTypeData(BaseStruct):
    name: str
    groupType: VoiceLangGroupType
