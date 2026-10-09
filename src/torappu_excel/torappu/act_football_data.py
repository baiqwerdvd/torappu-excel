from .evolve_phase import EvolvePhase
from .item_bundle import ItemBundle
from ..common import BaseStruct


class ActFootballData(BaseStruct):
    zoneAdditionDataMap: dict[str, "ActFootballData.ActFootballZoneAdditionData"]
    stageAdditionDataMap: dict[str, "ActFootballData.ActFootballStageAdditionData"]
    milestoneList: list["ActFootballData.ActFootballMilestoneItemData"]
    npcCharDataDict: dict[str, "ActFootballData.ActFootballNPCCharData"]
    constData: "ActFootballData.ActFootballConstData"

    class ActFootballZoneAdditionData(BaseStruct):
        zoneId: str
        unlockText: str

    class ActFootballStageAdditionData(BaseStruct):
        stageId: str
        selfTeamIcon: str
        selfTeamName: str
        enemyTeamIcon: str
        enemyTeamName: str
        unlockBuffId: str | None
        unlockBuffIcon: str | None
        unlockBuffName: str | None
        unlockBuffDesc: str | None
        firstCompletePoint: int
        completePoint: int

    class ActFootballMilestoneItemData(BaseStruct):
        milestoneId: str
        orderId: int
        tokenNum: int
        reward: ItemBundle
        availTime: int

    class ActFootballNPCCharData(BaseStruct):
        instId: int
        charId: str
        level: int
        evolvePhase: EvolvePhase
        mainSkillLevel: int
        specializeLevel: int
        potentialRank: int
        favorPoint: int
        skinId: str
        getTime: int

    class ActFootballConstData(BaseStruct):
        milestonePointId: str
        milestoneTrackId: str
