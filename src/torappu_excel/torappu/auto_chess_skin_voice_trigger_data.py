from .char_word_show_type import CharWordShowType
from ..common import BaseStruct


class AutoChessSkinVoiceTriggerData(BaseStruct):
    trigger: CharWordShowType
    probability: float
    cd: int
    priority: int
