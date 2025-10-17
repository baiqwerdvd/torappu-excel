from ..common import BaseStruct


class ActivityMiniStoryData(BaseStruct):
    tokenItemId: str
    zoneDescList: dict[str, "ActivityMiniStoryData.ZoneDescInfo"]
    favorUpList: dict[str, "ActivityMiniStoryData.FavorUpInfo"]
    extraDropZoneList: list[str]

    class ZoneDescInfo(BaseStruct):
        zoneId: str
        unlockText: str

    class FavorUpInfo(BaseStruct):
        charId: str
        displayStartTime: int
        displayEndTime: int
