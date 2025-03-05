from ..common import BaseStruct, CustomIntEnum


class Act9D0Data(BaseStruct):
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

    class ZoneDescInfo(BaseStruct):
        zoneId: str
        unlockText: str
        displayStartTime: int

    class FavorUpInfo(BaseStruct):
        charId: str
        displayStartTime: int
        displayEndTime: int

    class SubMissionInfo(BaseStruct):
        missionId: str
        missionTitle: str
        sortId: int
        missionIndex: str

    class ActivityNewsStyleInfo(BaseStruct):
        typeId: str
        typeName: str
        typeLogo: str
        typeMainLogo: str

    class ActivityNewsLine(BaseStruct):
        lineType: "Act9D0Data.ActivityNewsLineType"
        content: str

    class ActivityNewsInfo(BaseStruct):
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

    class ActivityNewsServerInfo(BaseStruct):
        newsId: str
        preposedStage: str

    class Act9D0ConstData(BaseStruct):
        campaignEnemyCnt: int
        campaignStageId: str | None
