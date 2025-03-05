from .char_word_show_type import CharWordShowType
from ..common import BaseStruct

from msgspec import field


class FestivalVoiceWeightData(BaseStruct):
    showType: CharWordShowType
    weight: float
    priority: int
    weightValue: float | None = field(default=None)
