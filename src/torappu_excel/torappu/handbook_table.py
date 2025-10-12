from pydantic import BaseModel, ConfigDict

from .data_unlock_type import DataUnlockTypeInt
from .handbook_info_text_view_data import HandBookInfoTextViewData


class StoryTextAudioInfoListItem(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    storyText: str | None
    storyTitle: str | None


class StoryTextAudioItem(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    stories: list[StoryTextAudioInfoListItem]
    unLockorNot: bool
    unLockType: DataUnlockTypeInt
    unLockParam: str
    unLockString: str


class CharHandbook(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    charID: str
    drawName: str
    infoName: str
    infoTextAudio: list[HandBookInfoTextViewData]
    storyTextAudio: list[StoryTextAudioItem]


class HandbookTable(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    char_102_texas: CharHandbook
