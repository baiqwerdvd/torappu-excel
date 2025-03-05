from .data_unlock_type import DataUnlockTypeInt
from .handbook_info_text_view_data import HandBookInfoTextViewData
from ..common import BaseStruct


class StoryTextAudioInfoListItem(BaseStruct):
    storyText: str | None
    storyTitle: str | None


class StoryTextAudioItem(BaseStruct):
    stories: list[StoryTextAudioInfoListItem]
    unLockorNot: bool
    unLockType: DataUnlockTypeInt
    unLockParam: str
    unLockString: str


class CharHandbook(BaseStruct):
    charID: str
    drawName: str
    infoName: str
    infoTextAudio: list[HandBookInfoTextViewData]
    storyTextAudio: list[StoryTextAudioItem]


class HandbookTable(BaseStruct):
    char_102_texas: CharHandbook
