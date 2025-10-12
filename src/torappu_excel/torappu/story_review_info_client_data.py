from pydantic import BaseModel, ConfigDict

from .item_type import ItemType
from .story_data import StoryData
from .story_review_type import StoryReviewType
from .story_review_unlock_type import StoryReviewUnlockType


class StoryReviewInfoClientData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    storyReviewType: StoryReviewType
    storyId: str
    storyGroup: str
    storySort: int
    storyDependence: str | None
    storyCanShow: int
    storyCode: str | None
    storyName: str
    storyPic: str | None
    storyInfo: str | None
    storyCanEnter: int
    storyTxt: str
    avgTag: str
    unLockType: StoryReviewUnlockType
    costItemType: ItemType
    costItemId: str | None
    costItemCount: int
    stageCount: int
    requiredStages: list[StoryData.Condition.StageCondition] | None
