from ..common import BaseStruct

from msgspec import field


class ActArchiveTimelineItemData(BaseStruct):
    timelineId: str
    timelineSortId: int
    timelineTitle: str
    timelineDes: str
    picIdList: list[str] | None = field(default=None)
    audioIdList: list[str] | None = field(default=None)
    avgIdList: list[str] | None = field(default=None)
    storyIdList: list[str] | None = field(default=None)
    newsIdList: list[str] | None = field(default=None)
