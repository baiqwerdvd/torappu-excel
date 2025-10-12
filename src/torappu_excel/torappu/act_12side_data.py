from enum import StrEnum

from pydantic import BaseModel, ConfigDict

from .item_bundle import ItemBundle


class Act12SideData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    constData: "Act12SideData.ConstData"
    zoneAdditionDataList: list["Act12SideData.ZoneAdditionData"]
    missionDescList: dict[str, "Act12SideData.MissionDescInfo"]
    mileStoneInfoList: list["Act12SideData.MileStoneInfo"]
    photoList: dict[str, "Act12SideData.PhotoInfo"]
    recycleDialogDict: dict["Act12SideData.RecycleDialogType", list["Act12SideData.RecycleDialogData"]]

    class ActZoneClass(StrEnum):
        NONE = "NONE"
        NORMAL = "NORMAL"
        HIGHLEVEL = "HIGHLEVEL"
        SUB = "SUB"

    class RecycleDialogType(StrEnum):
        NONE = "NONE"
        EMPTY = "EMPTY"
        LOW = "LOW"
        MEDIUM = "MEDIUM"
        HIGH = "HIGH"
        GACHA = "GACHA"

    class RecycleAnimationState(StrEnum):
        NONE = "NONE"
        NORMAL = "NORMAL"
        SMILE = "SMILE"

    class ConstData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        recycleRewardThreshold: int
        charmRepoUnlockStageId: str
        recycleLowThreshold: int
        recycleMediumThreshold: int
        recycleHighThreshold: int
        autoGetCharmId: str
        fogStageId: str
        fogUnlockStageId: str
        fogUnlockTs: int
        fogUnlockDesc: str

    class ZoneAdditionData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        zoneId: str
        unlockText: str
        zoneClass: "Act12SideData.ActZoneClass"

    class MissionDescInfo(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        zoneClass: "Act12SideData.ActZoneClass"
        specialMissionDesc: str
        needLock: bool
        unlockHint: str | None
        unlockStage: str | None

    class MileStoneInfo(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        mileStoneId: str
        orderId: int
        tokenNum: int
        item: ItemBundle
        isPrecious: bool
        mileStoneStage: int

    class PhotoInfo(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        picId: str
        picName: str
        mileStoneId: str
        picDesc: str
        jumpStageId: str | None

    class RecycleDialogData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        dialogType: "Act12SideData.RecycleDialogType"
        dialog: str
        dialogExpress: "Act12SideData.RecycleAnimationState"
