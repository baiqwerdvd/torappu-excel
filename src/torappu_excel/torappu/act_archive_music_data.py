from .act_archive_music_item_data import ActArchiveMusicItemData
from ..common import BaseStruct


class ActArchiveMusicData(BaseStruct):
    musics: dict[str, ActArchiveMusicItemData]
