from msgspec import field

from ..common import BaseStruct


class StorylineSSData(BaseStruct):
    desc: str
    backgroundId: str
    tags: list[str]
    reopenActivityId: str | None
    retroActivityId: str | None
    isRecommended: bool
    recommendHideStageId: str | None
    overrideStageList: list[str] | None
    name: str | None = field(default=None)
