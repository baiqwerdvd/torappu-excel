from pydantic import BaseModel, ConfigDict, Field

from .char_word_show_type import CharWordShowType


class FestivalVoiceWeightData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    showType: CharWordShowType
    weight: float
    priority: int
    weightValue: float | None = Field(default=None)
