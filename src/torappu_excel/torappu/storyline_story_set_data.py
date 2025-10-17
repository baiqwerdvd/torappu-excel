from .item_type import ItemType
from .storyline_collect_data import StorylineCollectData
from .storyline_mainline_data import StorylineMainlineData
from .storyline_ssdata import StorylineSSData
from .storyline_story_set_type import StorylineStorySetType
from ..common import BaseStruct


class StorylineStorySetData(BaseStruct):
    storySetId: str
    storySetType: StorylineStorySetType
    sortByYear: int
    sortWithinYear: int
    kvImageId: str
    titleImageId: str
    haveVideoToPlay: bool
    backgroundId: str | None
    gameMusicId: str | None
    coreRewardType: ItemType
    coreRewardId: str | None
    relevantActivityId: str | None
    mainlineData: StorylineMainlineData | None
    ssData: StorylineSSData | None
    collectData: StorylineCollectData | None
