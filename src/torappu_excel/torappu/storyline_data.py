from .storyline_location_data import StorylineLocationData
from .storyline_type import StorylineType
from ..common import BaseStruct


class StorylineData(BaseStruct):
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
