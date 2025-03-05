from .item_bundle import ItemBundle
from .story_review_entry_type import StoryReviewEntryType
from .story_review_info_client_data import StoryReviewInfoClientData
from .story_review_type import StoryReviewType
from ..common import BaseStruct

from msgspec import field


class StoryReviewGroupClientData(BaseStruct):
    id_: str = field(name="id")
    name: str
    entryType: StoryReviewEntryType
    actType: StoryReviewType
    startTime: int
    endTime: int
    startShowTime: int
    endShowTime: int
    remakeStartTime: int
    remakeEndTime: int
    storyEntryPicId: str | None
    storyPicId: str | None
    storyMainColor: str | None
    customType: int
    storyCompleteMedalId: str | None
    rewards: list[ItemBundle] | None
    infoUnlockDatas: list[StoryReviewInfoClientData]
