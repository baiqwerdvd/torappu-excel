from pydantic import BaseModel, ConfigDict

from .storyline_location_type import StorylineLocationType
from .storyline_mainline_split_data import StorylineMainlineSplitData


class StorylineLocationData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    locationId: str
    locationType: StorylineLocationType
    sortId: int
    startTime: int
    presentStageId: str | None
    unlockStageId: str | None
    relevantStorySetId: str | None
    mainlineSplitData: StorylineMainlineSplitData | None
