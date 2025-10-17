from .storyline_location_type import StorylineLocationType
from .storyline_mainline_split_data import StorylineMainlineSplitData
from ..common import BaseStruct


class StorylineLocationData(BaseStruct):
    locationId: str
    locationType: StorylineLocationType
    sortId: int
    startTime: int
    presentStageId: str | None
    unlockStageId: str | None
    relevantStorySetId: str | None
    mainlineSplitData: StorylineMainlineSplitData | None
