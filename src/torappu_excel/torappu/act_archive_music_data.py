from pydantic import BaseModel, ConfigDict

from .act_archive_music_item_data import ActArchiveMusicItemData


class ActArchiveMusicData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    musics: dict[str, ActArchiveMusicItemData]
