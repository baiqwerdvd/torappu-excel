from .item_bundle import ItemBundle
from .item_type import ItemType
from .quest_stage_data import QuestStageData
from .rune_table import RuneTable
from .stage_data import StageData
from ..common import BaseStruct, CustomIntEnum

from msgspec import field


class Act24SideData(BaseStruct):
    class MeldingGoodDisplayType(CustomIntEnum):
        NONE = "NONE", 0
        RARE_1 = "RARE_1", 1
        RARE_2 = "RARE_2", 2
        RARE_3 = "RARE_3", 3

    class MeldingGoodGachaType(CustomIntEnum):
        NONE = "NONE", 0
        LIMITED = "LIMITED", 1
        UNLIMITED = "UNLIMITED", 2

    class MissionType(CustomIntEnum):
        NONE = "NONE", 0
        HUNTING_TASK = "HUNTING_TASK", 1
        COLLECTION_TASK = "COLLECTION_TASK", 2
        EXPLORATION_TASK = "EXPLORATION_TASK", 3

    class MeldingItemRarityType(CustomIntEnum):
        NONE = "NONE", 0
        RARITY_1 = "RARITY_1", 1
        RARITY_2 = "RARITY_2", 2
        RARITY_3 = "RARITY_3", 3
        RARITY_4 = "RARITY_4", 4
        RARITY_5 = "RARITY_5", 5
        RARITY_6 = "RARITY_6", 6

    toolDataList: dict[str, "Act24SideData.ToolData"]
    mealDataList: dict[str, "Act24SideData.MealData"]
    meldingDict: dict[str, "Act24SideData.MeldingItemData"]
    meldingGachaBoxDataList: dict[str, "Act24SideData.MeldingGachaBoxData"]
    meldingGachaBoxGoodDataMap: dict[str, list["Act24SideData.MeldingGachaBoxGoodData"]]
    mealWelcomeTxtDataMap: dict[str, str]
    zoneAdditionDataMap: dict[str, "Act24SideData.ZoneAdditionData"]
    questStageList: list[QuestStageData]
    missionDataList: dict[str, "Act24SideData.MissionExtraData"]
    meldingDropDict: dict[str, StageData.StageDropInfo]
    stageMapPreviewDict: dict[str, list[str]]
    constData: "Act24SideData.ConstData"

    class ToolData(BaseStruct):
        toolId: str
        sortId: int
        toolName: str
        toolDesc: str
        toolIcon1: str
        toolIcon2: str
        toolUnlockDesc: str
        toolBuffId: str
        runeData: "RuneTable.PackedRuneData"
        toolStageId: str | None = field(default=None)

    class MealData(BaseStruct):
        mealId: str
        sortId: int
        mealName: str
        mealEffectDesc: str
        mealDesc: str
        mealIcon: str
        mealCost: int
        mealRewardAP: int
        mealRewardItemInfo: ItemBundle

    class MeldingItemData(BaseStruct):
        meldingId: str
        sortId: int
        meldingPrice: int
        rarity: "Act24SideData.MeldingItemRarityType"

    class MeldingGachaBoxData(BaseStruct):
        gachaBoxId: str
        gachaSortId: int
        gachaIcon: str
        gachaBoxName: str
        gachaCost: int
        gachaTimesLimit: int
        themeColor: str
        remainItemBgColor: str

    class MeldingGachaBoxGoodData(BaseStruct):
        goodId: str
        gachaBoxId: str
        orderId: int
        itemId: str
        itemType: ItemType
        displayType: "Act24SideData.MeldingGoodDisplayType"
        perCount: int
        totalCount: int
        gachaType: "Act24SideData.MeldingGoodGachaType"
        weight: int
        gachaOrderId: int
        gachaNum: int

    class ZoneAdditionData(BaseStruct):
        zoneId: str
        zoneIcon: str
        unlockText: str
        displayTime: str

    class MissionExtraData(BaseStruct):
        taskTypeName: str
        taskTypeIcon: str
        taskType: "Act24SideData.MissionType"
        taskTitle: str
        taskClient: str
        taskClientDesc: str

    class ConstData(BaseStruct):
        stageUnlockToolDesc: str
        mealLackMoney: str
        mealDayTimesLimit: int
        toolMaximum: int
        stageCanNotUseToTool: list[str]
        gachaDefaultProb: float | int
        gachaExtraProb: float | int
