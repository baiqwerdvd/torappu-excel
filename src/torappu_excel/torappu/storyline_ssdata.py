from ..common import BaseStruct


class StorylineSSData(BaseStruct):
    name: str
    desc: str
    backgroundId: str
    tags: list[str]
    reopenActivityId: str | None
    retroActivityId: str | None
    isRecommended: bool
    recommendHideStageId: str | None
    overrideStageList: list[str] | None
