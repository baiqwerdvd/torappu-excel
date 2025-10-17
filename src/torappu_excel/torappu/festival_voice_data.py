from msgspec import field

from .char_word_show_type import CharWordShowType
from .festival_time_data import FestivalTimeData
from ..common import BaseStruct


class FestivalVoiceData(BaseStruct):
    showType: CharWordShowType
    timeData: list[FestivalTimeData]
    startTs: int | None = field(default=None)
    endTs: int | None = field(default=None)
