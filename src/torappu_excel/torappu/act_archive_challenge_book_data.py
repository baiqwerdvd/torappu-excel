from .act_archive_challenge_book_item_data import ActArchiveChallengeBookItemData
from ..common import BaseStruct


class ActArchiveChallengeBookData(BaseStruct):
    stories: dict[str, ActArchiveChallengeBookItemData]
