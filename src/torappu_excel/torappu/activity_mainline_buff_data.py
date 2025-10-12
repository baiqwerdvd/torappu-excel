from pydantic import BaseModel, ConfigDict


class ActivityMainlineBuffData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    missionGroupList: dict[str, "ActivityMainlineBuffData.MissionGroupData"]
    periodDataList: list["ActivityMainlineBuffData.PeriodData"]
    apSupplyOutOfDateDict: dict[str, int]
    constData: "ActivityMainlineBuffData.ConstData"

    class MissionGroupData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        id: str
        bindBanner: str
        sortId: int
        zoneId: str
        missionIdList: list[str]

    class PeriodDataStepData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        isBlock: bool
        favorUpDesc: str | None
        unlockDesc: str | None
        bindStageId: str | None
        blockDesc: str | None

    class PeriodData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        id: str
        startTime: int
        endTime: int
        favorUpCharDesc: str
        favorUpImgName: str
        newChapterImgName: str
        newChapterZoneId: str | None
        stepDataList: list["ActivityMainlineBuffData.PeriodDataStepData"]

    class ConstData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        favorUpStageRange: str
