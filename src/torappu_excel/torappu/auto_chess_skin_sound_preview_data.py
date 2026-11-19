from .char_word_show_type import CharWordShowType
from ..common import BaseStruct


class AutoChessSkinSoundPreviewData(BaseStruct):
    soundId: str
    sortId: int
    title: str
    voiceUse: str
    voiceId: str
    placeType: CharWordShowType
    sfxModule: str
    sfxPlaySignal: str
    sfxSubSignal: str
