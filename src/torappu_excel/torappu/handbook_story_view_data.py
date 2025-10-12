from pydantic import BaseModel, ConfigDict

from .data_unlock_type import DataUnlockType


class HandBookStoryViewData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    stories: list["HandBookStoryViewData.StoryText"]
    storyTitle: str
    unLockorNot: bool

    class StoryText(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        storyText: str
        unLockType: DataUnlockType
        unLockParam: str
        showType: DataUnlockType
        showParam: str
        unLockString: str
        patchIdList: list[str] | None
