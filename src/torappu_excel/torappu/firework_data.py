from pydantic import BaseModel, ConfigDict

from torappu_excel.common import CustomIntEnum

from .grid_position import GridPosition


class FireworkData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

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

    class PlateContent(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        plateContent: list[GridPosition]

    class PlateSlotData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        id: str
        idx: int

    class PlateData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        plateId: str
        sortId: int
        directionType: "FireworkData.FireworkDirectionType"
        unlockLevel: str | None
        plateRank: int
        plateContents: list["FireworkData.PlateContent"]
        isCraft: bool

    class AnimalData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

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

    class LevelData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        levelId: str
        sortId: int
        trapPosX: int
        trapPosY: int
        isSPLevel: bool

    class ConstData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        maxFireworkNum: int
        maxFireworkPlateRowCount: int
        unlockStageCode: str
        dontDisplayFireworkPluginStageList: list[str]
