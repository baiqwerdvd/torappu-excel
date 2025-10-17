from msgspec import field

from .char_word_show_type import CharWordShowType
from ..common import BaseStruct


class FestivalVoiceWeightData(BaseStruct):
    showType: CharWordShowType
    weight: float
    priority: int
    weightValue: float | None = field(default=None)
