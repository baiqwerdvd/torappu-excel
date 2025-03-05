from .handbook_avg_group_data import HandbookAvgGroupData
from .handbook_story_view_data import HandBookStoryViewData
from ..common import BaseStruct

from msgspec import field


class HandbookInfoData(BaseStruct):
    charID: str
    infoName: str
    storyTextAudio: list[HandBookStoryViewData]
    handbookAvgList: list[HandbookAvgGroupData]
    isLimited: bool | None = field(default=None)
