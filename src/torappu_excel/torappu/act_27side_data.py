from .item_bundle import ItemBundle
from ..common import BaseStruct

from msgspec import field


class Act27SideData(BaseStruct):
    goodDataMap: dict[str, "Act27SideData.Act27SideGoodData"]
    mileStoneList: list["Act27SideData.Act27SideMileStoneData"]
    goodLaunchDataList: list["Act27SideData.Act27SideGoodLaunchData"]
    shopDataMap: dict[str, "Act27SideData.Act27SideShopData"]
    inquireDataList: list["Act27SideData.Act27SideInquireData"]
    dynEntrySwitchData: list["Act27SideData.Act27SideDynEntrySwitchData"]
    zoneAdditionDataMap: dict[str, "Act27SideData.Act27sideZoneAdditionData"]
    constData: "Act27SideData.Act27SideConstData"

    class Act27SideGoodData(BaseStruct):
        id_: str = field(name="id")
        name: str
        typeDesc: str
        iconId: str
        launchIconId: str
        purchasePrice: list[int]
        sellingPriceList: list[int]
        sellShopList: list[str]
        isPermanent: bool

    class Act27SideMileStoneData(BaseStruct):
        mileStoneId: str
        mileStoneLvl: int
        needPointCnt: int
        rewardItem: ItemBundle

    class Act27SideGoodLaunchData(BaseStruct):
        groupId: str
        startTime: int
        stageId: str | None
        code: str | None
        drinkId: str
        foodId: str
        souvenirId: str

    class Act27SideShopData(BaseStruct):
        shopId: str
        sortId: int
        name: str
        iconId: str

    class Act27SideInquireData(BaseStruct):
        mileStonePt: int
        inquireCount: int

    class Act27SideDynEntrySwitchData(BaseStruct):
        entryId: str
        startHour: int
        signalId: str

    class Act27sideZoneAdditionData(BaseStruct):
        zoneId: str
        unlockText: str
        displayTime: str

    class Act27SideMileStoneFurniRewardData(BaseStruct):
        furniId: str
        pointNum: int

    class Act27SideConstData(BaseStruct):
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
