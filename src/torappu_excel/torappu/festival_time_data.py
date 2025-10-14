from pydantic import BaseModel, ConfigDict

from .festival_voice_time_type import FestivalVoiceTimeType


class FestivalTimeData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    timeType: FestivalVoiceTimeType
    interval: "FestivalTimeData.FestivalTimeInterval"

    class FestivalTimeInterval(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        startTs: int
        endTs: int
