from .festival_voice_time_type import FestivalVoiceTimeType
from ..common import BaseStruct


class FestivalTimeData(BaseStruct):
    class FestivalTimeInterval(BaseStruct):
        startTs: int
        endTs: int

    timeType: FestivalVoiceTimeType
    interval: "FestivalTimeData.FestivalTimeInterval"
