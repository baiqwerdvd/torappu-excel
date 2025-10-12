from enum import StrEnum

from pydantic import BaseModel, ConfigDict

from .item_bundle import ItemBundle
from .mission_data import MissionData
from .mission_group import MissionGroup
from .rune_table import RuneTable


class Act5D1Data(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    class GoodType(StrEnum):
        NORMAL = "NORMAL"
        PROGRESS = "PROGRESS"

    stageCommonData: list["Act5D1Data.RuneStageData"]
    runeStageData: list["Act5D1Data.RuneRecurrentStateData"]
    runeUnlockDict: dict[str, list["Act5D1Data.RuneUnlockData"]]
    runeReleaseData: list["Act5D1Data.RuneReleaseData"]
    missionData: list[MissionData]
    missionGroup: list[MissionGroup]
    useBenefitMissionDict: dict[str, bool]
    shopData: "Act5D1Data.ShopData"
    coinItemId: str
    ptItemId: str
    stageRune: list[RuneTable.RuneStageExtraData]
    showRuneMissionList: list[str]

    class RuneStageData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        stageId: str
        levelId: str
        code: str
        name: str
        loadingPicId: str
        description: str
        picId: str

    class RuneRecurrentStateData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        runeReId: str
        stageId: str
        slotId: int
        startTime: int
        endTime: int
        runeList: list[str]
        isAvail: bool
        warningPoint: int

    class RuneUnlockData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        runeId: str
        priceItem: ItemBundle
        runeName: str
        bgPic: str
        runeDesc: str
        sortId: int
        iconId: str

    class RuneReleaseData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        runeId: str
        stageId: str
        releaseTime: int

    class ShopGood(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        goodId: str
        slotId: int
        price: int
        availCount: int
        item: ItemBundle
        progressGoodId: str
        goodType: "Act5D1Data.GoodType"

    class ProgessGoodItem(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        order: int
        price: int
        displayName: str
        item: ItemBundle

    class ShopData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        shopGoods: dict[str, "Act5D1Data.ShopGood"]
        progressGoods: dict[str, list["Act5D1Data.ProgessGoodItem"]]
