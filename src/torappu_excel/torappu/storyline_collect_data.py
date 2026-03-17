from msgspec import field

from ..common import BaseStruct


class StorylineCollectData(BaseStruct):
    desc: str
    backgroundId: str
    name: str | None = field(default=None)
