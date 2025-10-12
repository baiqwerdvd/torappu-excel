from pydantic import BaseModel, ConfigDict

from .storyline_location_data import StorylineLocationData
from .storyline_type import StorylineType


class StorylineData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    storylineId: str
    storylineType: StorylineType
    sortId: int
    storylineName: str
    storylineIconId: str | None
    storylineLogoId: str
    backgroundId: str
    hasVideoToPlay: bool
    startTs: int
    locations: dict[str, StorylineLocationData]
