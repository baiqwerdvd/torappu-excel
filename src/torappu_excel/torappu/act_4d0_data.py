from pydantic import BaseModel, ConfigDict

from .item_bundle import ItemBundle


class Act4D0Data(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    mileStoneItemList: list["Act4D0Data.MileStoneItemInfo"]
    mileStoneStoryList: list["Act4D0Data.MileStoneStoryInfo"]
    storyInfoList: list["Act4D0Data.StoryInfo"]
    stageInfo: list["Act4D0Data.StageJumpInfo"]
    tokenItem: ItemBundle
    charStoneId: str
    apSupplyOutOfDateDict: dict[str, int]
    extraDropZones: list[str]

    class MileStoneItemInfo(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        mileStoneId: str
        orderId: int
        tokenNum: int
        item: ItemBundle

    class MileStoneStoryInfo(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        mileStoneId: str
        orderId: int
        tokenNum: int
        storyKey: str
        desc: str

    class StoryInfo(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        storyKey: str
        storyId: str
        storySort: str
        storyName: str
        lockDesc: str
        storyDesc: str

    class StageJumpInfo(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        stageKey: str
        zoneId: str
        stageId: str
        unlockDesc: str
        lockDesc: str
