from ..common import BaseStruct


class StorylineMainlineData(BaseStruct):
    zoneId: str | None
    retroId: str | None
    decoImageId: str
    desc: str
    backgroundId: str
    tags: list[str]
