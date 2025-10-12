from pydantic import BaseModel, ConfigDict, Field

from .char_word_show_type import CharWordShowType
from .festival_time_data import FestivalTimeData


class FestivalVoiceData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    showType: CharWordShowType
    timeData: list[FestivalTimeData]
    startTs: int | None = Field(default=None)
    endTs: int | None = Field(default=None)
