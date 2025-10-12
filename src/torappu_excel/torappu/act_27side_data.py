from pydantic import BaseModel, ConfigDict

from .item_bundle import ItemBundle


class Act27SideData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    goodDataMap: dict[str, "Act27SideData.Act27SideGoodData"]
    mileStoneList: list["Act27SideData.Act27SideMileStoneData"]
    goodLaunchDataList: list["Act27SideData.Act27SideGoodLaunchData"]
    shopDataMap: dict[str, "Act27SideData.Act27SideShopData"]
    inquireDataList: list["Act27SideData.Act27SideInquireData"]
    dynEntrySwitchData: list["Act27SideData.Act27SideDynEntrySwitchData"]
    zoneAdditionDataMap: dict[str, "Act27SideData.Act27sideZoneAdditionData"]
    constData: "Act27SideData.Act27SideConstData"

    class Act27SideGoodData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        id: str
        name: str
        typeDesc: str
        iconId: str
        launchIconId: str
        purchasePrice: list[int]
        sellingPriceList: list[int]
        sellShopList: list[str]
        isPermanent: bool

    class Act27SideMileStoneData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        mileStoneId: str
        mileStoneLvl: int
        needPointCnt: int
        rewardItem: ItemBundle

    class Act27SideGoodLaunchData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        groupId: str
        startTime: int
        stageId: str | None
        code: str | None
        drinkId: str
        foodId: str
        souvenirId: str

    class Act27SideShopData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        shopId: str
        sortId: int
        name: str
        iconId: str

    class Act27SideInquireData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        mileStonePt: int
        inquireCount: int

    class Act27SideDynEntrySwitchData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        entryId: str
        startHour: int
        signalId: str

    class Act27sideZoneAdditionData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        zoneId: str
        unlockText: str
        displayTime: str

    class Act27SideMileStoneFurniRewardData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        furniId: str
        pointNum: int

    class Act27SideConstData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        stageId: str
        stageCode: str
        purchasePriceName: list[str]
        furniRewardList: list["Act27SideData.Act27SideMileStoneFurniRewardData"]
        prizeText: str
        playerShopId: str
        milestonePointName: str
        inquirePanelTitle: str
        inquirePanelDesc: str
        gain123: list[float]
        gain113: list[float]
        gain122: list[float]
        gain111: list[float]
        gain11None: list[float]
        gain12None: list[float]
        campaignEnemyCnt: int
