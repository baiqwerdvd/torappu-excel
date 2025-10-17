from .grid_position import GridPosition
from ..common import BaseStruct, CustomIntEnum


class FireworkData(BaseStruct):
    class FireworkDirectionType(CustomIntEnum):
        TWO_DIR = "TWO_DIR", 0
        FOUR_DIR = "FOUR_DIR", 1

    class FireworkType(CustomIntEnum):
        RED = "RED", 0
        BLUE = "BLUE", 1
        YELLOW = "YELLOW", 2
        GREEN = "GREEN", 3

    plateData: dict[str, "FireworkData.PlateData"]
    animalData: dict[str, "FireworkData.AnimalData"]
    levelData: dict[str, "FireworkData.LevelData"]
    constData: "FireworkData.ConstData"

    class PlateContent(BaseStruct):
        plateContent: list[GridPosition]

    class PlateSlotData(BaseStruct):
        id: str
        idx: int

    class PlateData(BaseStruct):
        plateId: str
        sortId: int
        directionType: "FireworkData.FireworkDirectionType"
        unlockLevel: str | None
        plateRank: int
        plateContents: list["FireworkData.PlateContent"]
        isCraft: bool

    class AnimalData(BaseStruct):
        animalId: str
        sortId: int
        animalName: str
        animalBuffDesc1: str
        animalBuffDesc2: str
        unlockLevel: str | None
        type: "FireworkData.FireworkType"
        noneOutlineUnselectIconId: list[str]
        outlineIconId: list[str]
        noneOutlineSelectIconId: list[str]
        unlockToast: str
        unlockToastIconId: str
        changedToast: str
        fireworkAnimalNameIconId: str

    class LevelData(BaseStruct):
        levelId: str
        sortId: int
        trapPosX: int
        trapPosY: int
        isSPLevel: bool

    class ConstData(BaseStruct):
        maxFireworkNum: int
        maxFireworkPlateRowCount: int
        unlockStageCode: str
        dontDisplayFireworkPluginStageList: list[str]
