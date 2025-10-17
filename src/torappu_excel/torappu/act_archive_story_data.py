from .act_archive_story_item_data import ActArchiveStoryItemData
from ..common import BaseStruct


class ActArchiveStoryData(BaseStruct):
    stories: dict[str, ActArchiveStoryItemData]
