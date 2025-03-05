from .char_extra_word_data import CharExtraWordData
from .char_word_data import CharWordData
from .char_word_show_type import CharWordShowType
from .extra_voice_config_data import ExtraVoiceConfigData
from .festival_voice_data import FestivalVoiceData
from .festival_voice_weight_data import FestivalVoiceWeightData
from .new_voice_time_data import NewVoiceTimeData
from .voice_lang_data import VoiceLangData
from .voice_lang_group_data import VoiceLangGroupData
from .voice_lang_group_type import VoiceLangGroupType
from .voice_lang_type import VoiceLangType
from .voice_lang_type_data import VoiceLangTypeData
from ..common import BaseStruct


class CharwordTable(BaseStruct):
    charWords: dict[str, CharWordData]
    charExtraWords: dict[str, CharExtraWordData]
    voiceLangDict: dict[str, VoiceLangData]
    defaultLangType: VoiceLangType
    newTagList: list[str]
    voiceLangTypeDict: dict[VoiceLangType, VoiceLangTypeData]
    voiceLangGroupTypeDict: dict[VoiceLangGroupType, VoiceLangGroupData]
    charDefaultTypeDict: dict[str, VoiceLangType]
    startTimeWithTypeDict: dict[VoiceLangType, list[NewVoiceTimeData]]
    displayGroupTypeList: list[VoiceLangGroupType]
    displayTypeList: list[VoiceLangType]
    playVoiceRange: CharWordShowType
    fesVoiceData: dict[str, FestivalVoiceData] | list[FestivalVoiceData]
    fesVoiceWeight: dict[str, FestivalVoiceWeightData]
    extraVoiceConfigData: dict[str, ExtraVoiceConfigData]
