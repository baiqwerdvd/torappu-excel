# pyright: reportMissingTypeArgument=false
from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field

from torappu_excel.common import CustomIntEnum

from .grid_position import GridPosition
from .item_bundle import ItemBundle
from .item_rarity import ItemRarity
from .shared_models import CharacterData as ShareCharacterData


class BuildingData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

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
    categoryNames: dict[str, str]
    buffSortData: dict[str, "BuildingData.BuildingRoomTypeBuffSortData"]

    class RoomUnlockCond(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        id: str
        number: dict[str, "BuildingData.RoomUnlockCond.CondItem"]

        class CondItem(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            type: "BuildingData.RoomType"
            level: int
            count: int

    class RoomData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        id: "BuildingData.RoomType"
        name: str
        description: str | None
        defaultPrefabId: str
        canLevelDown: bool
        maxCount: int
        category: "BuildingData.RoomCategory"
        size: GridPosition
        phases: list["BuildingData.RoomData.PhaseData"]

        class BuildCost(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            items: list[ItemBundle]
            time: int
            labor: int

        class PhaseData(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            overrideName: str | None
            overridePrefabId: str | None
            unlockCondId: str
            buildCost: "BuildingData.RoomData.BuildCost"
            electricity: int
            maxStationedNum: int
            manpowerCost: int

    class LayoutData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        id: str
        slots: dict[str, "BuildingData.LayoutData.RoomSlot"]
        cleanCosts: dict[str, "BuildingData.LayoutData.SlotCleanCost"]
        storeys: dict[str, "BuildingData.LayoutData.StoreyData"]

        class RoomSlot(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            id: str
            cleanCostId: str
            costLabor: int
            provideLabor: int
            size: GridPosition
            offset: GridPosition
            category: "BuildingData.RoomCategory"
            storeyId: str

        class SlotCleanCost(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            id: str
            number: dict[str, "BuildingData.LayoutData.SlotCleanCost.CountCost"]

            class CountCost(BaseModel):
                model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

                items: list[ItemBundle]

        class StoreyData(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            id: str
            yOffset: int
            unlockControlLevel: int
            type: "BuildingData.LayoutData.StoreyData.Type"

            class Type(StrEnum):
                UPGROUND = "UPGROUND"
                DOWNGROUND = "DOWNGROUND"

    class PrefabInfo(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        id: str
        blueprintRoomOverrideId: str | None
        size: GridPosition
        floorGridSize: GridPosition
        backWallGridSize: GridPosition
        obstacleId: str | None

    class ControlRoomBean(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        basicCostBuff: int
        phases: list | None = Field(default=None)

    class ManufactPhase(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        speed: float | int
        outputCapacity: int

    class ManufactRoomBean(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        basicSpeedBuff: float
        phases: list["BuildingData.ManufactPhase"]

    class ShopRoomBean(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        phases: list | None = Field(default=None)

    class HirePhase(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        economizeRate: float
        resSpeed: int
        refreshTimes: int

    class HireRoomBean(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        basicSpeedBuff: float
        phases: list["BuildingData.HirePhase"]

    class DormPhase(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        manpowerRecover: int
        decorationLimit: int

    class DormRoomBean(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        phases: list["BuildingData.DormPhase"]

    class PrivatePhase(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        decorationLimit: int

    class PrivateRoomBean(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        phases: list["BuildingData.PrivatePhase"]

    class MeetingPhase(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        friendSlotInc: int
        maxVisitorNum: int
        gatheringSpeed: int

    class MeetingRoomBean(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        basicSpeedBuff: float
        phases: list["BuildingData.MeetingPhase"]

    class TradingPhase(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        orderSpeed: float | int
        orderLimit: int
        orderRarity: int

    class TradingRoomBean(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        basicSpeedBuff: float
        phases: list["BuildingData.TradingPhase"]

    class WorkshopPhase(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        manpowerFactor: float | int

    class WorkShopRoomBean(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        phases: list["BuildingData.WorkshopPhase"]

    class TrainingPhase(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        specSkillLvlLimit: int

    class TrainingBean(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        basicSpeedBuff: float
        phases: list["BuildingData.TrainingPhase"]

    class PowerRoomBean(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        basicSpeedBuff: float
        phases: list | None = Field(default=None)

    class BuildingBuffCharSlot(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        buffData: list["BuildingData.BuildingBuffCharSlot.SlotItem"]

        class SlotItem(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            buffId: str
            cond: "ShareCharacterData.UnlockCondition"

    class BuildingCharacter(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        charId: str
        maxManpower: int
        buffChar: list["BuildingData.BuildingBuffCharSlot"]

    class BuildingBuff(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

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

    class WorkshopExtraWeightItem(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        itemId: str
        weight: int
        itemCount: int

    class CustomData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        furnitures: dict[str, "BuildingData.CustomData.FurnitureData"]
        themes: dict[str, "BuildingData.CustomData.ThemeData"]
        groups: dict[str, "BuildingData.CustomData.GroupData"]
        types: dict[str, "BuildingData.CustomData.FurnitureTypeData"]
        subTypes: dict[str, "BuildingData.CustomData.FurnitureSubTypeData"]
        defaultFurnitures: dict[str, list["BuildingData.CustomData.DormitoryDefaultFurnitureItem"]]
        interactGroups: dict[str, list["BuildingData.CustomData.InteractItem"]]
        diyUISortTemplates: dict[str, dict[str, "BuildingData.CustomData.DiyUISortTemplateListData"]]

        class FurnitureData(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            id: str
            sortId: int
            name: str
            iconId: str
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
            processedByProductGroup: list["BuildingData.WorkshopExtraWeightItem"]
            canBeDestroy: bool
            isOnly: int
            quantity: int
            musicId: str
            enableRoomType: int
            interactType: "BuildingData.FurnitureInteract | None" = None

        class ThemeQuickSetupItem(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            furnitureId: str
            pos0: int
            pos1: int
            dir: int

        class ThemeData(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            id: str
            enableRoomType: int
            sortId: int
            name: str
            themeType: str
            desc: str
            quickSetup: list["BuildingData.CustomData.ThemeQuickSetupItem"]
            groups: list[str]
            furnitures: list[str]

        class GroupData(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            id: str
            sortId: int
            name: str
            themeId: str
            comfort: int
            count: int
            furniture: list[str]

        class FurnitureTypeData(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            type: "BuildingData.FurnitureType"
            name: str
            enableRoomType: int

        class FurnitureSubTypeData(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            subType: "BuildingData.FurnitureSubType"
            name: str
            type: "BuildingData.FurnitureType"
            sortId: int
            countLimit: int
            enableRoomType: int

        class DormitoryDefaultFurnitureItem(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            furnitureId: str
            xOffset: int
            yOffset: int
            defaultPrefabId: str

        class InteractItem(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            skinId: str

        class DiyUISortTemplateListData(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            diySortType: "BuildingData.DiySortType"
            expandState: str
            defaultTemplateIndex: int
            defaultTemplateOrder: "BuildingData.DiyUISortOrder"
            templates: list["BuildingData.CustomData.DiyUISortTemplateListData.DiyUISortTemplateData"]
            diyUIType: "BuildingData.DiyUIType | None" = None

            class DiyUISortTemplateData(BaseModel):
                model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

                name: str
                sequences: list[str]
                stableSequence: str
                stableSequenceOrder: str

    class ManufactFormula(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

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

        class UnlockRoom(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            roomId: str
            roomLevel: int
            roomCount: int

        class UnlockStage(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            stageId: str
            rank: int

    class ShopFormula(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

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

        class UnlockRoom(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            roomId: "BuildingData.RoomType"
            roomLevel: int
            roomCount: int

        class UnlockStage(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            stageId: str
            rank: int

    class WorkshopFormula(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

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

        class UnlockRoom(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            roomId: str
            roomLevel: int
            roomCount: int

        class UnlockStage(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            stageId: str
            rank: int

    class CreditFormula(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        initiative: dict
        passive: dict

        class ValueModel(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            basic: int
            addition: int

    class WorkshopRarityInfo(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        name: str
        order: int
        rarityList: list[ItemRarity]
        color: str

    class SlotPrequeData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        roomType: "BuildingData.RoomType"
        name: str
        typeSortId: int
        isPreque: bool
        prequeNum: int

    class DormitoryPrequeData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        roomType: "BuildingData.RoomType"
        name: str

    class StationManageConstData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

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

    class StationManageFilterInfo(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        charStationFilterType: "BuildingData.CharStationFilterType"
        name: str

    class MusicSingleData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        bgmId: str
        bgmSortId: int
        bgmStartTime: int
        bgmName: str
        gameMusicId: str
        obtainApproach: str
        bgmDescUnlocked: str
        unlockType: str
        unlockParams: list[str]

    class MusicData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        defaultMusic: str
        musicDatas: dict[str, "BuildingData.MusicSingleData"]

    class BuildingRoomTypeBuffSortData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        hasEfficiencySort: bool
        defaultGroupSortId: int
        efficiencyTargetDict: dict[str, "BuildingData.BuildingRoomTypeBuffSortData.buffGroupInfo"]

        class buffGroupInfo(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            targets: list[str]
            sortId: int
