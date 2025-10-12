from pydantic import BaseModel, ConfigDict

from torappu_excel.common import CustomIntEnum


class Act9D0Data(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    class ActivityNewsLineType(CustomIntEnum):
        TextContent = "TextContent", 0
        ImageContent = "ImageContent", 1

    tokenItemId: str
    zoneDescList: dict[str, "Act9D0Data.ZoneDescInfo"]
    favorUpList: dict[str, "Act9D0Data.FavorUpInfo"]
    subMissionInfo: dict[str, "Act9D0Data.SubMissionInfo"] | None
    hasSubMission: bool
    apSupplyOutOfDateDict: dict[str, int]
    newsInfoList: dict[str, "Act9D0Data.ActivityNewsInfo"] | None
    newsServerInfoList: dict[str, "Act9D0Data.ActivityNewsServerInfo"] | None
    miscHub: dict[str, str]
    constData: "Act9D0Data.Act9D0ConstData"

    class ZoneDescInfo(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        zoneId: str
        unlockText: str
        displayStartTime: int

    class FavorUpInfo(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        charId: str
        displayStartTime: int
        displayEndTime: int

    class SubMissionInfo(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        missionId: str
        missionTitle: str
        sortId: int
        missionIndex: str

    class ActivityNewsStyleInfo(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        typeId: str
        typeName: str
        typeLogo: str
        typeMainLogo: str

    class ActivityNewsLine(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        lineType: "Act9D0Data.ActivityNewsLineType"
        content: str

    class ActivityNewsInfo(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        newsId: str
        newsSortId: int
        styleInfo: "Act9D0Data.ActivityNewsStyleInfo"
        preposedStage: str | None
        titlePic: str
        newsTitle: str
        newsInfShow: int
        newsFrom: str
        newsText: str
        newsParam1: int
        newsParam2: int
        newsParam3: float
        newsLines: list["Act9D0Data.ActivityNewsLine"]

    class ActivityNewsServerInfo(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        newsId: str
        preposedStage: str

    class Act9D0ConstData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        campaignEnemyCnt: int
        campaignStageId: str | None
