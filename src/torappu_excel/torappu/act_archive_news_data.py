from .act_archive_news_item_data import ActArchiveNewsItemData
from ..common import BaseStruct


class ActArchiveNewsData(BaseStruct):
    news: dict[str, ActArchiveNewsItemData]
