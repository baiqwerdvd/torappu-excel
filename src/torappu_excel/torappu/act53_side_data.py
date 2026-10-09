from ..common import BaseStruct


class Act53SideData(BaseStruct):
    zoneAdditionDataMap: dict[str, "Act53SideData.Act53SideZoneAdditionData"]
    actOdcStageIdList: list[str]
    constData: "Act53SideData.Act53SideConstData"

    class Act53SideZoneAdditionData(BaseStruct):
        zoneId: str
        unlockText: str

    class Act53SideConstData(BaseStruct):
        arkOdcTopicId: str
        arkOdcUnlockStageId: str
        arkOdcUnlockText: str
        arkOdcUpdateText: str
        campaignStageId: str
        campaignEnemyCnt: int
        coinItemId: str
