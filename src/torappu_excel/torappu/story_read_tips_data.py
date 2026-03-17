from ..common import BaseStruct


class StoryReadTipsData(BaseStruct):
    key: str
    picId: str
    mainText: str
    confirmText: str
    isAll: bool
    stageIdList: list[str]
