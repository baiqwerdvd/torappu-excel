from pydantic import BaseModel, ConfigDict, Field

from .handbook_unlock_param import HandbookUnlockParam
from .item_bundle import ItemBundle


class HandbookStoryStageData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    charId: str
    code: str
    description: str
    levelId: str
    loadingPicId: str
    name: str
    rewardItem: list[ItemBundle]
    stageGetTime: int
    stageId: str
    unlockParam: list[HandbookUnlockParam]
    zoneId: str
    zoneNameForShow: str | None = Field(default=None)
    stageNameForShow: str | None = Field(default=None)
    picId: str | None = Field(default=None)
