# pyright: reportMissingTypeArgument=false
from enum import StrEnum

from .grid_position import GridPosition
from .item_bundle import ItemBundle
from .item_rarity import ItemRarity
from .shared_models import CharacterData as ShareCharacterData
from ..common import BaseStruct, CustomIntEnum

from msgspec import field


class BuildingData(BaseStruct):
    class RoomType(CustomIntEnum):
        NONE = "NONE", 0
        CONTROL = "CONTROL", 1
        POWER = "POWER", 2
        MANUFACTURE = "MANUFACTURE", 4
        SHOP = "SHOP", 8
        DORMITORY = "DORMITORY", 16
        MEETING = "MEETING", 32
        HIRE = "HIRE", 64
        ELEVATOR = "ELEVATOR", 128
        CORRIDOR = "CORRIDOR", 256
        TRADING = "TRADING", 512
        WORKSHOP = "WORKSHOP", 1024
        TRAINING = "TRAINING", 2048
        FUNCTIONAL = "FUNCTIONAL", 3710
        PRIVATE = "PRIVATE", 4096
        ALL = "ALL", 8191

    class RoomCategory(CustomIntEnum):
        NONE = "NONE", 0
        FUNCTION = "FUNCTION", 1
        OUTPUT = "OUTPUT", 2
        CUSTOM = "CUSTOM", 4
        ELEVATOR = "ELEVATOR", 8
        CORRIDOR = "CORRIDOR", 16
        SPECIAL = "SPECIAL", 32
        CUSTOM_P = "CUSTOM_P", 64
        ELEVATOR_P = "ELEVATOR_P", 128
        CORRIDOR_P = "CORRIDOR_P", 256
        ALL = "ALL", 511

    class BuffCategory(StrEnum):
        NONE = "NONE"
        FUNCTION = "FUNCTION"
        OUTPUT = "OUTPUT"
        RECOVERY = "RECOVERY"

    class FurnitureInteract(CustomIntEnum):
        NONE = "NONE", 0
        ANIMATOR = "ANIMATOR", 1
        MUSIC = "MUSIC", 2
        FUNCTION = "FUNCTION", 3

    class FurnitureType(CustomIntEnum):
        FLOOR = "FLOOR", 0
        CARPET = "CARPET", 1
        SEATING = "SEATING", 2
        BEDDING = "BEDDING", 3
        TABLE = "TABLE", 4
        CABINET = "CABINET", 5
        DECORATION = "DECORATION", 6
        WALLPAPER = "WALLPAPER", 7
        WALLDECO = "WALLDECO", 8
        WALLLAMP = "WALLLAMP", 9
        CEILING = "CEILING", 10
        CEILINGLAMP = "CEILINGLAMP", 11
        FUNCTION = "FUNCTION", 12
        INTERACT = "INTERACT", 13

    class FurnitureSubType(CustomIntEnum):
        NONE = "NONE", 0
        CHAIR = "CHAIR", 1
        SOFA = "SOFA", 2
        BARSTOOL = "BARSTOOL", 3
        STOOL = "STOOL", 4
        BENCH = "BENCH", 5
        ORTHER_S = "ORTHER_S", 6
        POSTER = "POSTER", 7
        CURTAIN = "CURTAIN", 8
        BOARD_WD = "BOARD_WD", 9
        SHELF = "SHELF", 10
        INSTRUMENT_WD = "INSTRUMENT_WD", 11
        ART_WD = "ART_WD", 12
        PLAQUE = "PLAQUE", 13
        CONTRACT = "CONTRACT", 14
        ANNIHILATION = "ANNIHILATION", 15
        ORTHER_WD = "ORTHER_WD", 16
        FLOORLAMP = "FLOORLAMP", 17
        PLANT = "PLANT", 18
        PARTITION = "PARTITION", 19
        COOKING = "COOKING", 20
        CATERING = "CATERING", 21
        DEVICE = "DEVICE", 22
        INSTRUMENT_D = "INSTRUMENT_D", 23
        ART_D = "ART_D", 24
        BOARD_D = "BOARD_D", 25
        ENTERTAINMENT = "ENTERTAINMENT", 26
        STORAGE = "STORAGE", 27
        DRESSING = "DRESSING", 28
        WARM = "WARM", 29
        WASH = "WASH", 30
        ORTHER_D = "ORTHER_D", 31
        COLUMN = "COLUMN", 32
        DECORATION_C = "DECORATION_C", 33
        CURTAIN_C = "CURTAIN_C", 34
        DEVICE_C = "DEVICE_C", 35
        CONTRACT_2 = "CONTRACT_2", 36
        LIGHT = "LIGHT", 37
        ORTHER_C = "ORTHER_C", 38
        VISITOR = "VISITOR", 39
        MUSIC = "MUSIC", 40

    class FurnitureLocation(CustomIntEnum):
        NONE = "NONE", 0
        WALL = "WALL", 1
        FLOOR = "FLOOR", 2
        CARPET = "CARPET", 3
        CEILING = "CEILING", 4
        POSTER = "POSTER", 5
        CEILINGDECAL = "CEILINGDECAL", 6

    class FurnitureCategory(StrEnum):
        FURNITURE = "FURNITURE"
        WALL = "WALL"
        FLOOR = "FLOOR"

    class DiyUIType(StrEnum):
        MENU = "MENU"
        THEME = "THEME"
        FURNITURE = "FURNITURE"
        FURNITURE_IN_THEME = "FURNITURE_IN_THEME"
        RECENT_THEME = "RECENT_THEME"
        RECENT_FURNITURE = "RECENT_FURNITURE"
        PRESET = "PRESET"

    class DiySortType(CustomIntEnum):
        NONE = "NONE", 0
        THEME = "THEME", 1
        FURNITURE = "FURNITURE", 2
        FURNITURE_IN_THEME = "FURNITURE_IN_THEME", 3
        RECENT_THEME = "RECENT_THEME", 4
        RECENT_FURNITURE = "RECENT_FURNITURE", 5
        MEETING_THEME = "MEETING_THEME", 6
        MEETING_FURNITURE = "MEETING_FURNITURE", 7
        MEETING_FURNITURE_IN_THEME = "MEETING_FURNITURE_IN_THEME", 8
        MEETING_RECENT_THEME = "MEETING_RECENT_THEME", 9
        MEETING_RECENT_FURNITURE = "MEETING_RECENT_FURNITURE", 10

    class DiyUISortOrder(StrEnum):
        DESC = "DESC"
        ASC = "ASC"

    class FormulaItemType(StrEnum):
        NONE = "NONE"
        F_EVOLVE = "F_EVOLVE"
        F_BUILDING = "F_BUILDING"
        F_GOLD = "F_GOLD"
        F_DIAMOND = "F_DIAMOND"
        F_FURNITURE = "F_FURNITURE"
        F_EXP = "F_EXP"
        F_ASC = "F_ASC"
        F_SKILL = "F_SKILL"

    class CharStationFilterType(CustomIntEnum):
        All = "All", 0
        DormLock = "DormLock", 1
        NotStationed = "NotStationed", 2

    controlSlotId: str
    meetingSlotId: str
    initMaxLabor: int
    laborRecoverTime: int
    manufactInputCapacity: int
    shopCounterCapacity: int
    comfortLimit: int
    creditInitiativeLimit: int
    creditPassiveLimit: int
    creditComfortFactor: int
    creditGuaranteed: int
    creditCeiling: int
    manufactUnlockTips: str
    shopUnlockTips: str
    manufactStationBuff: float
    comfortManpowerRecoverFactor: int
    manpowerDisplayFactor: int
    shopOutputRatio: dict[str, int] | None
    shopStackRatio: dict[str, int] | None
    basicFavorPerDay: int
    humanResourceLimit: int
    tiredApThreshold: int
    processedCountRatio: int
    tradingStrategyUnlockLevel: int
    tradingReduceTimeUnit: int
    tradingLaborCostUnit: int
    manufactReduceTimeUnit: int
    manufactLaborCostUnit: int
    laborAssistUnlockLevel: int
    apToLaborUnlockLevel: int
    apToLaborRatio: int
    socialResourceLimit: int
    socialSlotNum: int
    furniDuplicationLimit: int
    assistFavorReport: int
    manufactManpowerCostByNum: list[int]
    tradingManpowerCostByNum: list[int]
    trainingBonusMax: int
    betaRemoveTime: int
    furniHighlightTime: float
    canNotVisitToast: str
    musicPlayerOpenTime: int
    roomsWithoutRemoveStaff: list[str]
    privateFavorLevelThresholds: list[int]
    roomUnlockConds: dict[str, "BuildingData.RoomUnlockCond"]
    rooms: dict[str, "BuildingData.RoomData"]
    layouts: dict[str, "BuildingData.LayoutData"]
    prefabs: dict[str, "BuildingData.PrefabInfo"]
    controlData: "BuildingData.ControlRoomBean"
    manufactData: "BuildingData.ManufactRoomBean"
    shopData: "BuildingData.ShopRoomBean"
    hireData: "BuildingData.HireRoomBean"
    dormData: "BuildingData.DormRoomBean"
    privateRoomData: "BuildingData.PrivateRoomBean"
    meetingData: "BuildingData.MeetingRoomBean"
    tradingData: "BuildingData.TradingRoomBean"
    workshopData: "BuildingData.WorkShopRoomBean"
    trainingData: "BuildingData.TrainingBean"
    powerData: "BuildingData.PowerRoomBean"
    chars: dict[str, "BuildingData.BuildingCharacter"]
    buffs: dict[str, "BuildingData.BuildingBuff"]
    workshopBonus: dict[str, list[str]]
    customData: "BuildingData.CustomData"
    manufactFormulas: dict[str, "BuildingData.ManufactFormula"]
    shopFormulas: dict[str, "BuildingData.ShopFormula"]
    workshopFormulas: dict[str, "BuildingData.WorkshopFormula"]
    creditFormula: "BuildingData.CreditFormula"
    goldItems: dict[str, int]
    assistantUnlock: list[int]
    workshopRarities: list["BuildingData.WorkshopRarityInfo"]
    todoItemSortPriorityDict: dict[str, int]
    slotPrequeDatas: dict[str, "BuildingData.SlotPrequeData"]
    dormitoryPrequeDatas: dict[str, "BuildingData.DormitoryPrequeData"]
    workshopTargetDesDict: dict[str, str]
    tradingOrderDesDict: dict[str, str]
    stationManageConstData: "BuildingData.StationManageConstData"
    stationManageFilterInfos: dict[str, "BuildingData.StationManageFilterInfo"]
    musicData: "BuildingData.MusicData"
    emojis: list[str]

    class RoomUnlockCond(BaseStruct):
        id_: str = field(name="id")
        number: dict[str, "BuildingData.RoomUnlockCond.CondItem"]

        class CondItem(BaseStruct):
            type_: "BuildingData.RoomType" = field(name="type")
            level: int
            count: int

    class RoomData(BaseStruct):
        id_: "BuildingData.RoomType" = field(name="id")
        name: str
        description: str | None
        defaultPrefabId: str
        canLevelDown: bool
        maxCount: int
        category: "BuildingData.RoomCategory"
        size: GridPosition
        phases: list["BuildingData.RoomData.PhaseData"]

        class BuildCost(BaseStruct):
            items: list[ItemBundle]
            time: int
            labor: int

        class PhaseData(BaseStruct):
            overrideName: str | None
            overridePrefabId: str | None
            unlockCondId: str
            buildCost: "BuildingData.RoomData.BuildCost"
            electricity: int
            maxStationedNum: int
            manpowerCost: int

    class LayoutData(BaseStruct):
        id_: str = field(name="id")
        slots: dict[str, "BuildingData.LayoutData.RoomSlot"]
        cleanCosts: dict[str, "BuildingData.LayoutData.SlotCleanCost"]
        storeys: dict[str, "BuildingData.LayoutData.StoreyData"]

        class RoomSlot(BaseStruct):
            id_: str = field(name="id")
            cleanCostId: str
            costLabor: int
            provideLabor: int
            size: GridPosition
            offset: GridPosition
            category: "BuildingData.RoomCategory"
            storeyId: str

        class SlotCleanCost(BaseStruct):
            id_: str = field(name="id")
            number: dict[str, "BuildingData.LayoutData.SlotCleanCost.CountCost"]

            class CountCost(BaseStruct):
                items: list[ItemBundle]

        class StoreyData(BaseStruct):
            id_: str = field(name="id")
            yOffset: int
            unlockControlLevel: int
            type_: "BuildingData.LayoutData.StoreyData.Type" = field(name="type")

            class Type(StrEnum):
                UPGROUND = "UPGROUND"
                DOWNGROUND = "DOWNGROUND"

    class PrefabInfo(BaseStruct):
        id_: str = field(name="id")
        blueprintRoomOverrideId: str | None
        size: GridPosition
        floorGridSize: GridPosition
        backWallGridSize: GridPosition
        obstacleId: str | None

    class ControlRoomBean(BaseStruct):
        basicCostBuff: int
        phases: list | None = field(default=None)

    class ManufactPhase(BaseStruct):
        speed: float | int
        outputCapacity: int

    class ManufactRoomBean(BaseStruct):
        basicSpeedBuff: float
        phases: list["BuildingData.ManufactPhase"]

    class ShopRoomBean(BaseStruct):
        phases: list | None = field(default=None)

    class HirePhase(BaseStruct):
        economizeRate: float
        resSpeed: int
        refreshTimes: int

    class HireRoomBean(BaseStruct):
        basicSpeedBuff: float
        phases: list["BuildingData.HirePhase"]

    class DormPhase(BaseStruct):
        manpowerRecover: int
        decorationLimit: int

    class DormRoomBean(BaseStruct):
        phases: list["BuildingData.DormPhase"]

    class PrivatePhase(BaseStruct):
        decorationLimit: int

    class PrivateRoomBean(BaseStruct):
        phases: list["BuildingData.PrivatePhase"]

    class MeetingPhase(BaseStruct):
        friendSlotInc: int
        maxVisitorNum: int
        gatheringSpeed: int

    class MeetingRoomBean(BaseStruct):
        basicSpeedBuff: float
        phases: list["BuildingData.MeetingPhase"]

    class TradingPhase(BaseStruct):
        orderSpeed: float | int
        orderLimit: int
        orderRarity: int

    class TradingRoomBean(BaseStruct):
        basicSpeedBuff: float
        phases: list["BuildingData.TradingPhase"]

    class WorkshopPhase(BaseStruct):
        manpowerFactor: float | int

    class WorkShopRoomBean(BaseStruct):
        phases: list["BuildingData.WorkshopPhase"]

    class TrainingPhase(BaseStruct):
        specSkillLvlLimit: int

    class TrainingBean(BaseStruct):
        basicSpeedBuff: float
        phases: list["BuildingData.TrainingPhase"]

    class PowerRoomBean(BaseStruct):
        basicSpeedBuff: float
        phases: list | None = field(default=None)

    class BuildingBuffCharSlot(BaseStruct):
        buffData: list["BuildingData.BuildingBuffCharSlot.SlotItem"]

        class SlotItem(BaseStruct):
            buffId: str
            cond: "ShareCharacterData.UnlockCondition"

    class BuildingCharacter(BaseStruct):
        charId: str
        maxManpower: int
        buffChar: list["BuildingData.BuildingBuffCharSlot"]

    class BuildingBuff(BaseStruct):
        buffId: str
        buffName: str
        buffIcon: str
        skillIcon: str
        sortId: int
        buffColor: str
        textColor: str
        buffCategory: "BuildingData.BuffCategory"
        roomType: "BuildingData.RoomType"
        description: str

    class WorkshopExtraWeightItem(BaseStruct):
        itemId: str
        weight: int
        itemCount: int

    class CustomData(BaseStruct):
        furnitures: dict[str, "BuildingData.CustomData.FurnitureData"]
        themes: dict[str, "BuildingData.CustomData.ThemeData"]
        groups: dict[str, "BuildingData.CustomData.GroupData"]
        types: dict[str, "BuildingData.CustomData.FurnitureTypeData"]
        subTypes: dict[str, "BuildingData.CustomData.FurnitureSubTypeData"]
        defaultFurnitures: dict[str, list["BuildingData.CustomData.DormitoryDefaultFurnitureItem"]]
        interactGroups: dict[str, list["BuildingData.CustomData.InteractItem"]]
        diyUISortTemplates: dict[str, dict[str, "BuildingData.CustomData.DiyUISortTemplateListData"]]

        class FurnitureData(BaseStruct):
            id_: str = field(name="id")
            sortId: int
            name: str
            iconId: str
            type_: "BuildingData.FurnitureType" = field(name="type")
            subType: "BuildingData.FurnitureSubType"
            location: "BuildingData.FurnitureLocation"
            category: "BuildingData.FurnitureCategory"
            validOnRotate: bool
            enableRotate: bool
            rarity: int
            themeId: str
            groupId: str
            width: int
            depth: int
            height: int
            comfort: int
            usage: str
            description: str
            obtainApproach: str
            processedProductId: str
            processedProductCount: int
            processedByProductPercentage: int
            processedByProductGroup: list["BuildingData.WorkshopExtraWeightItem"]
            canBeDestroy: bool
            isOnly: int
            quantity: int
            musicId: str
            enableRoomType: int
            interactType: "BuildingData.FurnitureInteract | None" = None

        class ThemeQuickSetupItem(BaseStruct):
            furnitureId: str
            pos0: int
            pos1: int
            dir_: int = field(name="dir")

        class ThemeData(BaseStruct):
            id_: str = field(name="id")
            enableRoomType: int
            sortId: int
            name: str
            themeType: str
            desc: str
            quickSetup: list["BuildingData.CustomData.ThemeQuickSetupItem"]
            groups: list[str]
            furnitures: list[str]

        class GroupData(BaseStruct):
            id_: str = field(name="id")
            sortId: int
            name: str
            themeId: str
            comfort: int
            count: int
            furniture: list[str]

        class FurnitureTypeData(BaseStruct):
            type_: "BuildingData.FurnitureType" = field(name="type")
            name: str
            enableRoomType: int

        class FurnitureSubTypeData(BaseStruct):
            subType: "BuildingData.FurnitureSubType"
            name: str
            type_: "BuildingData.FurnitureType" = field(name="type")
            sortId: int
            countLimit: int
            enableRoomType: int

        class DormitoryDefaultFurnitureItem(BaseStruct):
            furnitureId: str
            xOffset: int
            yOffset: int
            defaultPrefabId: str

        class InteractItem(BaseStruct):
            skinId: str

        class DiyUISortTemplateListData(BaseStruct):
            diySortType: "BuildingData.DiySortType"
            expandState: str
            defaultTemplateIndex: int
            defaultTemplateOrder: "BuildingData.DiyUISortOrder"
            templates: list["BuildingData.CustomData.DiyUISortTemplateListData.DiyUISortTemplateData"]
            diyUIType: "BuildingData.DiyUIType | None" = None

            class DiyUISortTemplateData(BaseStruct):
                name: str
                sequences: list[str]
                stableSequence: str
                stableSequenceOrder: str

    class ManufactFormula(BaseStruct):
        formulaId: str
        itemId: str
        count: int
        weight: int
        costPoint: int
        formulaType: "BuildingData.FormulaItemType"
        buffType: str
        costs: list[ItemBundle]
        requireRooms: list["BuildingData.ManufactFormula.UnlockRoom"]
        requireStages: list["BuildingData.ManufactFormula.UnlockStage"]

        class UnlockRoom(BaseStruct):
            roomId: str
            roomLevel: int
            roomCount: int

        class UnlockStage(BaseStruct):
            stageId: str
            rank: int

    class ShopFormula(BaseStruct):
        formulaId: str
        itemId: str
        count: int
        weight: int
        costPoint: int
        formulaType: "BuildingData.FormulaItemType"
        buffType: str
        costs: list[ItemBundle]
        requireRooms: list["BuildingData.ShopFormula.UnlockRoom"]
        requireStages: list["BuildingData.ShopFormula.UnlockStage"]

        class UnlockRoom(BaseStruct):
            roomId: "BuildingData.RoomType"
            roomLevel: int
            roomCount: int

        class UnlockStage(BaseStruct):
            stageId: str
            rank: int

    class WorkshopFormula(BaseStruct):
        sortId: int
        formulaId: str
        rarity: int
        itemId: str
        count: int
        goldCost: int
        apCost: int
        formulaType: "BuildingData.FormulaItemType"
        buffType: str
        extraOutcomeRate: float
        extraOutcomeGroup: list["BuildingData.WorkshopExtraWeightItem"]
        costs: list[ItemBundle]
        requireRooms: list["BuildingData.WorkshopFormula.UnlockRoom"]
        requireStages: list["BuildingData.WorkshopFormula.UnlockStage"]

        class UnlockRoom(BaseStruct):
            roomId: str
            roomLevel: int
            roomCount: int

        class UnlockStage(BaseStruct):
            stageId: str
            rank: int

    class CreditFormula(BaseStruct):
        initiative: dict
        passive: dict

        class ValueModel(BaseStruct):
            basic: int
            addition: int

    class WorkshopRarityInfo(BaseStruct):
        name: str
        order: int
        rarityList: list[ItemRarity]
        color: str

    class SlotPrequeData(BaseStruct):
        roomType: "BuildingData.RoomType"
        name: str
        typeSortId: int
        isPreque: bool
        prequeNum: int

    class DormitoryPrequeData(BaseStruct):
        roomType: "BuildingData.RoomType"
        name: str

    class StationManageConstData(BaseStruct):
        cantWorkToastNoTiredChar: str
        cantWorkToastNoAvailQueue: str
        cantWorkToastNoNeed: str
        cantRestToastNoTiredChar: str
        cantRestToastNoAvailDorm: str
        workBatchToast: str
        restBatchToast: str
        roomNoAvailQueueToast: str
        cantUseNoPerson: str
        cantUseWorking: str
        queueCleared: str
        updateTime: int
        dormLockUpdateTime: int

    class StationManageFilterInfo(BaseStruct):
        charStationFilterType: "BuildingData.CharStationFilterType"
        name: str

    class MusicSingleData(BaseStruct):
        bgmId: str
        bgmSortId: int
        bgmStartTime: int
        bgmName: str
        gameMusicId: str
        obtainApproach: str
        bgmDescUnlocked: str
        unlockType: str
        unlockParams: list[str]

    class MusicData(BaseStruct):
        defaultMusic: str
        musicDatas: dict[str, "BuildingData.MusicSingleData"]
