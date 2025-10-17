from .act_archive_timeline_item_data import ActArchiveTimelineItemData
from ..common import BaseStruct


class ActArchiveTimelineData(BaseStruct):
    timelineList: list[ActArchiveTimelineItemData]
