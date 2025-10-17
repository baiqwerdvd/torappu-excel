from enum import StrEnum

from .character_data import CharacterData
from .grid_position import GridPosition
from .item_bundle import ItemBundle
from .item_rarity import ItemRarity
from ..common import BaseStruct


class BuildingData(BaseStruct):
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
    shopData: "BuildingData.RoomBean_1"
    hireData: "BuildingData.HireRoomBean"
    dormData: "BuildingData.RoomBean_1"
    privateRoomData: "BuildingData.RoomBean_1"
    meetingData: "BuildingData.MeetingRoomBean"
    tradingData: "BuildingData.TradingRoomBean"
    workshopData: "BuildingData.RoomBean_1"
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
    workshopRarities: "list[BuildingData.WorkshopRarityInfo]"
    todoItemSortPriorityDict: dict[str, int]
    slotPrequeDatas: dict[str, "BuildingData.SlotPrequeData"]
    dormitoryPrequeDatas: dict[str, "BuildingData.DormitoryPrequeData"]
    workshopTargetDesDict: dict[str, str]
    tradingOrderDesDict: dict[str, str]
    stationManageConstData: "BuildingData.StationManageConstData"
    stationManageFilterInfos: dict[str, "BuildingData.StationManageFilterInfo"]
    musicData: "BuildingData.MusicData"
    emojis: list[str]
    categoryNames: dict[str, str]
    buffSortData: dict[str, "BuildingData.BuildingRoomTypeBuffSortData"]

    class RoomCategory(StrEnum):
        NONE = "NONE"
        FUNCTION = "FUNCTION"
        OUTPUT = "OUTPUT"
        CUSTOM = "CUSTOM"
        ELEVATOR = "ELEVATOR"
        CORRIDOR = "CORRIDOR"
        SPECIAL = "SPECIAL"
        CUSTOM_P = "CUSTOM_P"
        ELEVATOR_P = "ELEVATOR_P"
        CORRIDOR_P = "CORRIDOR_P"
        ALL = "ALL"

    class RoomTypeString(BaseStruct):
        pass

    class RoomType(StrEnum):
        NONE = "NONE"
        CONTROL = "CONTROL"
        POWER = "POWER"
        MANUFACTURE = "MANUFACTURE"
        SHOP = "SHOP"
        DORMITORY = "DORMITORY"
        MEETING = "MEETING"
        HIRE = "HIRE"
        ELEVATOR = "ELEVATOR"
        CORRIDOR = "CORRIDOR"
        TRADING = "TRADING"
        WORKSHOP = "WORKSHOP"
        TRAINING = "TRAINING"
        PRIVATE = "PRIVATE"
        FUNCTIONAL = "FUNCTIONAL"
        ALL = "ALL"

    class OrderType(StrEnum):
        O_COMPOUND = "O_COMPOUND"
        O_GOLD = "O_GOLD"
        O_DIAMOND = "O_DIAMOND"

    class FurnitureCategory(StrEnum):
        FURNITURE = "FURNITURE"
        WALL = "WALL"
        FLOOR = "FLOOR"

    class BuildingToDoType(StrEnum):
        NONE = "NONE"
        MANUF_STOP = "MANUF_STOP"
        TRADE_STOP = "TRADE_STOP"
        HIRE_EMPTY = "HIRE_EMPTY"
        MEETING_EMPTY = "MEETING_EMPTY"
        NEW_PRODUCTS = "NEW_PRODUCTS"
        HAS_ORDERS = "HAS_ORDERS"
        CHAR_TIRED = "CHAR_TIRED"
        TRAIN_FINISH = "TRAIN_FINISH"
        HIRE_REFRESHED = "HIRE_REFRESHED"
        NEW_CLUES = "NEW_CLUES"
        NEW_FAVOR = "NEW_FAVOR"
        NEW_FAVOR_MAX = "NEW_FAVOR_MAX"
        BATCH_WORK = "BATCH_WORK"
        BATCH_REST = "BATCH_REST"
        MESSAGE_BOARD = "MESSAGE_BOARD"

    class FurnitureType(StrEnum):
        FLOOR = "FLOOR"
        CARPET = "CARPET"
        SEATING = "SEATING"
        BEDDING = "BEDDING"
        TABLE = "TABLE"
        CABINET = "CABINET"
        DECORATION = "DECORATION"
        WALLPAPER = "WALLPAPER"
        WALLDECO = "WALLDECO"
        WALLLAMP = "WALLLAMP"
        CEILING = "CEILING"
        CEILINGLAMP = "CEILINGLAMP"
        FUNCTION = "FUNCTION"
        INTERACT = "INTERACT"

    class FurnitureSubType(StrEnum):
        NONE = "NONE"
        CHAIR = "CHAIR"
        SOFA = "SOFA"
        BARSTOOL = "BARSTOOL"
        STOOL = "STOOL"
        BENCH = "BENCH"
        ORTHER_S = "ORTHER_S"
        POSTER = "POSTER"
        CURTAIN = "CURTAIN"
        BOARD_WD = "BOARD_WD"
        SHELF = "SHELF"
        INSTRUMENT_WD = "INSTRUMENT_WD"
        ART_WD = "ART_WD"
        PLAQUE = "PLAQUE"
        CONTRACT = "CONTRACT"
        ANNIHILATION = "ANNIHILATION"
        ORTHER_WD = "ORTHER_WD"
        FLOORLAMP = "FLOORLAMP"
        PLANT = "PLANT"
        PARTITION = "PARTITION"
        COOKING = "COOKING"
        CATERING = "CATERING"
        DEVICE = "DEVICE"
        INSTRUMENT_D = "INSTRUMENT_D"
        ART_D = "ART_D"
        BOARD_D = "BOARD_D"
        ENTERTAINMENT = "ENTERTAINMENT"
        STORAGE = "STORAGE"
        DRESSING = "DRESSING"
        WARM = "WARM"
        WASH = "WASH"
        ORTHER_D = "ORTHER_D"
        COLUMN = "COLUMN"
        DECORATION_C = "DECORATION_C"
        CURTAIN_C = "CURTAIN_C"
        DEVICE_C = "DEVICE_C"
        CONTRACT_2 = "CONTRACT_2"
        LIGHT = "LIGHT"
        ORTHER_C = "ORTHER_C"
        VISITOR = "VISITOR"
        MUSIC = "MUSIC"

    class IRoomBean(BaseStruct):
        pass

    class FurnitureLocation(StrEnum):
        NONE = "NONE"
        WALL = "WALL"
        FLOOR = "FLOOR"
        CARPET = "CARPET"
        CEILING = "CEILING"
        POSTER = "POSTER"
        CEILINGDECAL = "CEILINGDECAL"

    class FurnitureInteract(StrEnum):
        NONE = "NONE"
        ANIMATOR = "ANIMATOR"
        MUSIC = "MUSIC"
        FUNCTION = "FUNCTION"

    class ObstaclePoint(BaseStruct):
        offset: GridPosition
        edgeWalkableMask: int

    class ObstacleRect(BaseStruct):
        pos: GridPosition
        size: GridPosition
        edgeWalkableMask: int

    class ObstacleData(BaseStruct):
        floorObstacles: "list[BuildingData.ObstaclePoint]"
        backwallObstacles: "list[BuildingData.ObstaclePoint]"

    class BuildingLocalData(BaseStruct):
        furnitureObstacleData: dict[str, "BuildingData.ObstacleData"]
        roomObstacleData: dict[str, "BuildingData.ObstacleData"]
        furnitureLODConfig: dict[str, "BuildingData.FurnitureLODConfig"]

    class FurnitureLODConfig(BaseStruct):
        showedObjNames: dict["BuildingData.LODLEVEL", list[str]]
        isOverWrite: bool

    class LODLEVEL(StrEnum):
        HIGHEST = "HIGHEST"
        HIGH = "HIGH"
        LOW = "LOW"
        LOWEST = "LOWEST"
        COUNT = "COUNT"

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

    class DiySortType(StrEnum):
        NONE = "NONE"
        THEME = "THEME"
        FURNITURE = "FURNITURE"
        FURNITURE_IN_THEME = "FURNITURE_IN_THEME"
        RECENT_THEME = "RECENT_THEME"
        RECENT_FURNITURE = "RECENT_FURNITURE"
        MEETING_THEME = "MEETING_THEME"
        MEETING_FURNITURE = "MEETING_FURNITURE"
        MEETING_FURNITURE_IN_THEME = "MEETING_FURNITURE_IN_THEME"
        MEETING_RECENT_THEME = "MEETING_RECENT_THEME"
        MEETING_RECENT_FURNITURE = "MEETING_RECENT_FURNITURE"

    class DiyUIType(StrEnum):
        MENU = "MENU"
        THEME = "THEME"
        FURNITURE = "FURNITURE"
        FURNITURE_IN_THEME = "FURNITURE_IN_THEME"
        RECENT_THEME = "RECENT_THEME"
        RECENT_FURNITURE = "RECENT_FURNITURE"
        PRESET = "PRESET"

    class DiyUISortOrder(StrEnum):
        DESC = "DESC"
        ASC = "ASC"

    class PrefabInfo(BaseStruct):
        id: str
        blueprintRoomOverrideId: str | None
        size: GridPosition
        floorGridSize: GridPosition
        backWallGridSize: GridPosition
        obstacleId: str | None

    class RoomUnlockCond(BaseStruct):
        id: str
        number: dict[str, "BuildingData.RoomUnlockCond.CondItem"]

        class CondItem(BaseStruct):
            type: "BuildingData.RoomType"
            level: int
            count: int

    class RoomData(BaseStruct):
        id: "BuildingData.RoomType"
        name: str
        description: str | None
        defaultPrefabId: str
        canLevelDown: bool
        maxCount: int
        category: "BuildingData.RoomCategory"
        size: GridPosition
        phases: "list[BuildingData.RoomData.PhaseData]"

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
        id: str
        slots: dict[str, "BuildingData.LayoutData.RoomSlot"]
        cleanCosts: dict[str, "BuildingData.LayoutData.SlotCleanCost"]
        storeys: dict[str, "BuildingData.LayoutData.StoreyData"]

        class RoomSlot(BaseStruct):
            id: str
            cleanCostId: str
            costLabor: int
            provideLabor: int
            size: GridPosition
            offset: GridPosition
            category: "BuildingData.RoomCategory"
            storeyId: str

        class SlotCleanCost(BaseStruct):
            id: str
            number: dict[str, "BuildingData.LayoutData.SlotCleanCost.CountCost"]

            class CountCost(BaseStruct):
                items: list[ItemBundle]

        class StoreyData(BaseStruct):
            id: str
            yOffset: int
            unlockControlLevel: int
            type: "BuildingData.LayoutData.StoreyData.Type"

            class Type(StrEnum):
                UPGROUND = "UPGROUND"
                DOWNGROUND = "DOWNGROUND"

    class BuffCategory(StrEnum):
        NONE = "NONE"
        FUNCTION = "FUNCTION"
        OUTPUT = "OUTPUT"
        RECOVERY = "RECOVERY"

    class BuildingCharacter(BaseStruct):
        charId: str
        maxManpower: int
        buffChar: "list[BuildingData.BuildingBuffCharSlot]"

    class BuildingBuffCharSlot(BaseStruct):
        buffData: "list[BuildingData.BuildingBuffCharSlot.SlotItem]"

        class SlotItem(BaseStruct):
            buffId: str
            cond: "CharacterData.UnlockCondition"

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
        efficiency: int
        targetGroupSortId: int
        targets: list[str]

    class BuildingRoomTypeBuffSortData(BaseStruct):
        hasEfficiencySort: bool
        defaultGroupSortId: int
        efficiencyTargetDict: dict[str, "BuildingData.BuildingRoomTypeBuffSortData.buffGroupInfo"]

        class buffGroupInfo(BaseStruct):
            targets: list[str]
            sortId: int

    class RoomBeanParam(BaseStruct):
        pass

    class RoomBean_1(BaseStruct):
        phases: list[object] | None

    class ControlRoomBean(BaseStruct):
        basicCostBuff: int
        phases: "list[BuildingData.ControlRoomPhase] | None"

    class ControlRoomPhase(BaseStruct):
        pass

    class ManufactRoomBean(BaseStruct):
        basicSpeedBuff: float
        phases: "list[BuildingData.ManufactPhase]"

    class ManufactPhase(BaseStruct):
        speed: float
        outputCapacity: int

    class ShopPhase(BaseStruct):
        counterNum: int
        speed: float
        moneyCapacity: int

    class HireRoomBean(BaseStruct):
        basicSpeedBuff: float
        phases: "list[BuildingData.HirePhase]"

    class HirePhase(BaseStruct):
        economizeRate: float
        resSpeed: int
        refreshTimes: int

    class DormPhase(BaseStruct):
        manpowerRecover: int
        decorationLimit: int

    class PrivatePhase(BaseStruct):
        decorationLimit: int

    class MeetingRoomBean(BaseStruct):
        basicSpeedBuff: float
        phases: "list[BuildingData.MeetingPhase]"

    class MeetingPhase(BaseStruct):
        friendSlotInc: int
        maxVisitorNum: int
        gatheringSpeed: int

    class TradingRoomBean(BaseStruct):
        basicSpeedBuff: float
        phases: "list[BuildingData.TradingPhase]"

    class TradingPhase(BaseStruct):
        orderSpeed: float
        orderLimit: int
        orderRarity: int

    class WorkshopPhase(BaseStruct):
        manpowerFactor: float

    class TrainingBean(BaseStruct):
        basicSpeedBuff: float
        phases: "list[BuildingData.TrainingPhase]"

    class TrainingPhase(BaseStruct):
        specSkillLvlLimit: int

    class PowerRoomBean(BaseStruct):
        basicSpeedBuff: float
        phases: "list[BuildingData.PowerPhase] | None"

    class PowerPhase(BaseStruct):
        pass

    class CustomData(BaseStruct):
        furnitures: dict[str, "BuildingData.CustomData.FurnitureData"]
        themes: dict[str, "BuildingData.CustomData.ThemeData"]
        groups: dict[str, "BuildingData.CustomData.GroupData"]
        types: dict["BuildingData.FurnitureType", "BuildingData.CustomData.FurnitureTypeData"]
        subTypes: dict["BuildingData.FurnitureSubType", "BuildingData.CustomData.FurnitureSubTypeData"]
        defaultFurnitures: dict[str, "list[BuildingData.CustomData.DormitoryDefaultFurnitureItem]"]
        interactGroups: dict[str, "list[BuildingData.CustomData.InteractItem]"]
        diyUISortTemplates: dict[
            "BuildingData.DiySortType", dict[str, "BuildingData.CustomData.DiyUISortTemplateListData"]
        ]

        class FurnitureData(BaseStruct):
            id: str
            sortId: int
            name: str
            iconId: str
            interactType: "BuildingData.FurnitureInteract"
            musicId: str
            type: "BuildingData.FurnitureType"
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
            processedByProductGroup: "list[BuildingData.WorkshopExtraWeightItem]"
            canBeDestroy: bool
            isOnly: int
            enableRoomType: int
            quantity: int

        class ThemeData(BaseStruct):
            id: str
            enableRoomType: int
            sortId: int
            name: str
            themeType: str
            desc: str
            quickSetup: "list[BuildingData.CustomData.ThemeQuickSetupItem]"
            groups: list[str]
            furnitures: list[str]

        class GroupData(BaseStruct):
            id: str
            sortId: int
            name: str
            themeId: str
            comfort: int
            count: int
            furniture: list[str]

        class ThemeQuickSetupItem(BaseStruct):
            furnitureId: str
            pos0: int
            pos1: int
            dir: int

        class FurnitureTypeData(BaseStruct):
            type: "BuildingData.FurnitureType"
            name: str
            enableRoomType: int

        class FurnitureSubTypeData(BaseStruct):
            subType: "BuildingData.FurnitureSubType"
            name: str
            type: "BuildingData.FurnitureType"
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
            templates: "list[BuildingData.CustomData.DiyUISortTemplateListData.DiyUISortTemplateData]"

            class DiyUISortTemplateData(BaseStruct):
                name: str
                sequences: list[str]
                stableSequence: str
                stableSequenceOrder: "BuildingData.DiyUISortOrder"

    class ManufactFormula(BaseStruct):
        formulaId: str
        itemId: str
        count: int
        weight: int
        costPoint: int
        formulaType: "BuildingData.FormulaItemType"
        buffType: str
        costs: list[ItemBundle]
        requireRooms: "list[BuildingData.ManufactFormula.UnlockRoom]"
        requireStages: "list[BuildingData.ManufactFormula.UnlockStage]"

        class UnlockRoom(BaseStruct):
            roomId: "BuildingData.RoomType"
            roomLevel: int
            roomCount: int

        class UnlockStage(BaseStruct):
            stageId: str
            rank: int

    class WorkshopExtraWeightItem(BaseStruct):
        weight: int
        itemId: str
        itemCount: int

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
        extraOutcomeGroup: "list[BuildingData.WorkshopExtraWeightItem]"
        costs: list[ItemBundle]
        requireRooms: "list[BuildingData.WorkshopFormula.UnlockRoom]"
        requireStages: "list[BuildingData.WorkshopFormula.UnlockStage]"

        class UnlockRoom(BaseStruct):
            roomId: "BuildingData.RoomType"
            roomLevel: int
            roomCount: int

        class UnlockStage(BaseStruct):
            stageId: str
            rank: int

    class ShopFormula(BaseStruct):
        formulaId: str
        itemId: str
        formulaType: "BuildingData.FormulaItemType"
        costPoint: int
        gainItem: ItemBundle
        requireRooms: "list[BuildingData.ShopFormula.UnlockRoom]"

        class UnlockRoom(BaseStruct):
            roomId: "BuildingData.RoomType"
            roomLevel: int

    class CreditFormula(BaseStruct):
        initiative: dict[int, "BuildingData.CreditFormula.ValueModel"]
        passive: dict[int, "BuildingData.CreditFormula.ValueModel"]

        class ValueModel(BaseStruct):
            basic: int
            addition: int

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

    class WorkshopRarityInfo(BaseStruct):
        name: str
        order: int
        rarityList: list[ItemRarity]
        color: str

    class StationManageFilterInfo(BaseStruct):
        charStationFilterType: "BuildingData.CharStationFilterType"
        name: str

    class CharStationFilterType(StrEnum):
        All = "All"
        DormLock = "DormLock"
        NotStationed = "NotStationed"

    class MusicData(BaseStruct):
        defaultMusic: str
        musicDatas: dict[str, "BuildingData.MusicSingleData"]

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
