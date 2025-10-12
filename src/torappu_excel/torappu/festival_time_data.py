from pydantic import BaseModel, ConfigDict

from .festival_voice_time_type import FestivalVoiceTimeType


class FestivalTimeData(BaseModel):
    class FestivalTimeInterval(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        startTs: int
        endTs: int

    timeType: FestivalVoiceTimeType
    interval: "FestivalTimeData.FestivalTimeInterval"
