from .festival_voice_time_type import FestivalVoiceTimeType
from ..common import BaseStruct


class FestivalTimeData(BaseStruct):
    timeType: FestivalVoiceTimeType
    interval: "FestivalTimeData.FestivalTimeInterval"

    class FestivalTimeInterval(BaseStruct):
        startTs: int
        endTs: int
