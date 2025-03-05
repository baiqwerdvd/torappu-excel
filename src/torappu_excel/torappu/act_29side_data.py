from .item_bundle import ItemBundle
from ..common import BaseStruct, CustomIntEnum

from msgspec import field


class Act29SideData(BaseStruct):
    class Act29SideInvestType(CustomIntEnum):
        MAJOR = "MAJOR", 0
        RARE = "RARE", 1
        NORMAL = "NORMAL", 2

    class Act29SideProductType(CustomIntEnum):
        PRODUCT_TYPE_1 = "PRODUCT_TYPE_1", 0
        PRODUCT_TYPE_2 = "PRODUCT_TYPE_2", 1
        PRODUCT_TYPE_3 = "PRODUCT_TYPE_3", 2
        PRODUCT_TYPE_4 = "PRODUCT_TYPE_4", 3
        PRODUCT_TYPE_5 = "PRODUCT_TYPE_5", 4
        ENUM = "ENUM", 5

    class Act29SideOrcheType(CustomIntEnum):
        ORCHE_1 = "ORCHE_1", 0
        ORCHE_2 = "ORCHE_2", 1
        ORCHE_3 = "ORCHE_3", 2
        ENUM = "ENUM", 3

    fragDataMap: dict[str, "Act29SideData.Act29SideFragData"]
    orcheDataMap: dict[str, "Act29SideData.Act29SideOrcheData"]
    productGroupDataMap: dict[str, "Act29SideData.Act29SideProductGroupData"]
    productDataMap: dict[str, "Act29SideData.Act29SideProductData"]
    formDataMap: dict[str, "Act29SideData.Act29SideFormData"]
    investResultDataMap: dict[str, "Act29SideData.Act29SideInvestResultData"]
    investDataMap: dict[str, "Act29SideData.Act29SideInvestData"]
    majorInvestIdList: list[str]
    rareInvestIdList: list[str]
    constData: "Act29SideData.Act29SideConstData"
    zoneAdditionDataMap: dict[str, "Act29SideData.Act29SideZoneAdditionData"]
    musicDataMap: list["Act29SideData.Act29SideMusicData"]

    class Act29SideFragData(BaseStruct):
        fragId: str
        sortId: int
        fragName: str
        fragIcon: str
        fragStoreIcon: str

    class Act29SideOrcheData(BaseStruct):
        id_: str = field(name="id")
        name: str
        desc: str
        icon: str
        sortId: int
        orcheType: "Act29SideData.Act29SideOrcheType"

    class Act29SideProductGroupData(BaseStruct):
        groupId: str
        groupName: str
        groupIcon: str
        groupDesc: str
        defaultBgmSignal: str
        productList: list[str]
        groupEngName: str
        groupSmallName: str
        groupTypeIcon: str
        groupStoreIconId: str
        groupTypeBasePic: str
        groupTypeEyeIcon: str
        groupSortId: int
        formList: list[str]
        sheetId: str
        sheetNum: int
        sheetRotateSpd: float | int
        productType: "Act29SideData.Act29SideProductType"
        productDescColor: str
        playTintColor: str
        confirmTintColor: str
        confirmDescColor: str
        bagThemeColor: str

    class Act29SideProductData(BaseStruct):
        id_: str = field(name="id")
        orcheId: str | None
        groupId: str
        formId: str | None
        musicId: str

    class Act29SideFormData(BaseStruct):
        formId: str
        fragIdList: list[str]
        formDesc: str
        productIdDict: dict[str, str]
        withoutOrcheProductId: str
        groupId: str
        formSortId: int

    class Act29SideInvestResultData(BaseStruct):
        resultId: str
        resultTitle: str
        resultDesc1: str
        resultDesc2: str

    class Act29SideInvestData(BaseStruct):
        investId: str
        investType: "Act29SideData.Act29SideInvestType"
        investNpcName: str
        storyId: str
        investNpcPic: str
        investNpcAvatarPic: str
        majorNpcPic: str | None
        majorNpcBlackPic: str | None
        reward: ItemBundle | None
        investSucResultId: str | None
        investFailResultId: str
        investRareResultId: str | None

    class Act29SideConstData(BaseStruct):
        majorInvestUnlockItemName: str
        wrongTipsTriggerTime: int
        majorInvestCompleteImgId: str
        majorInvestUnknownAvatarId: str
        majorInvestDetailDesc1: str
        majorInvestDetailDesc2: str
        majorInvestDetailDesc3: str
        majorInvestDetailDesc4: str
        hiddenInvestImgId: str
        hiddenInvestHeadImgId: str
        hiddenInvestNpcName: str
        unlockLevelId: str
        investResultHint: str
        investUnlockText: str
        noOrcheDesc: str
        investTrackId: str | None

    class Act29SideZoneAdditionData(BaseStruct):
        zoneId: str
        unlockText: str

    class Act29SideMusicData(BaseStruct):
        groupId: str
        orcheId: str | None
        musicId: str
