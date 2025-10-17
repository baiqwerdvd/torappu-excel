from .data_unlock_type import DataUnlockType
from ..common import BaseStruct


class HandBookStoryViewData(BaseStruct):
    stories: list["HandBookStoryViewData.StoryText"]
    storyTitle: str
    unLockorNot: bool

    class StoryText(BaseStruct):
        storyText: str
        unLockType: DataUnlockType
        unLockParam: str
        showType: DataUnlockType
        showParam: str
        unLockString: str
        patchIdList: list[str] | None
