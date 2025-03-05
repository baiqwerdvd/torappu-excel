from enum import StrEnum

from .act_archive_type import ActArchiveType
from .item_bundle import ItemBundle
from .mission_display_rewards import MissionDisplayRewards
from .shared_models import ActivityTable
from ..common import BaseStruct

from msgspec import field


class Act13SideData(BaseStruct):
    constData: "Act13SideData.ConstData"
    orgDataMap: dict[str, "Act13SideData.OrgData"]
    principalDataMap: dict[str, "Act13SideData.PrincipalData"]
    longTermMissionDataMap: dict[str, "Act13SideData.LongTermMissionData"]
    dailyMissionDataList: list["Act13SideData.DailyMissionData"]
    dailyRewardGroupDataMap: dict[str, "Act13SideData.DailyMissionRewardGroupData"]
    archiveItemUnlockData: dict[str, "Act13SideData.ArchiveItemUnlockData"]
    hiddenAreaData: dict[str, ActivityTable.ActivityHiddenAreaData]
    zoneAddtionDataMap: dict[str, "Act13SideData.ZoneAdditionData"]

    class PrestigeRank(StrEnum):
        D = "D"
        C = "C"
        B = "B"
        A = "A"
        S = "S"

    class ActZoneClass(StrEnum):
        NONE = "NONE"
        NORMAL = "NORMAL"
        HIGHLEVEL = "HIGHLEVEL"
        SUB = "SUB"

    class UnlockCondition(StrEnum):
        NONE = "NONE"
        PRESTIGE = "PRESTIGE"
        STAGE = "STAGE"

    class ConstData(BaseStruct):
        prestigeDescList: list[str]
        dailyRandomCount: list[list[int]] | None
        dailyWeightInitial: int
        dailyWeightComplete: int
        agendaRecover: int
        agendaMax: int
        agendaHint: int
        missionPoolMax: int
        missionBoardMax: int
        itemRandomList: list[ItemBundle]
        unlockPrestigeCond: str
        hotSpotShowFlag: int

    class PrestigeData(BaseStruct):
        rank: "Act13SideData.PrestigeRank"
        threshold: int
        reward: ItemBundle | None
        newsCount: int
        archiveCount: int
        avgCount: int

    class LongTermMissionGroupData(BaseStruct):
        groupId: str
        groupName: str
        orgId: str
        missionList: list[str]

    class OrgSectionData(BaseStruct):
        sectionName: str
        sortId: int
        groupData: "Act13SideData.LongTermMissionGroupData"

    class OrgData(BaseStruct):
        orgId: str
        orgName: str
        orgEnName: str
        openTime: int
        principalIdList: list[str]
        prestigeList: list["Act13SideData.PrestigeData"]
        agendaCount2PrestigeItemMap: dict[str, "ItemBundle"]
        orgSectionList: list["Act13SideData.OrgSectionData"]
        prestigeItem: ItemBundle

    class PrincipalData(BaseStruct):
        principalId: str
        principalName: str
        principalEnName: str
        avgCharId: str
        principalDescList: list[str]

    class LongTermMissionData(BaseStruct):
        missionName: str
        groupId: str
        principalId: str
        finishedDesc: str
        sectionSortId: int
        haveStageBtn: bool
        jumpStageId: str | None

    class DailyMissionData(BaseStruct):
        id_: str = field(name="id")
        sortId: int
        description: str
        missionName: str
        template: str
        templateType: str
        param: list[str]
        rewards: list[MissionDisplayRewards] | None
        orgPool: list[str] | None
        rewardPool: list[str] | None
        jumpStageId: str
        agendaCount: int

    class DailyMissionRewardGroupData(BaseStruct):
        groupId: str
        rewards: list[ItemBundle]

    class ArchiveItemUnlockData(BaseStruct):
        itemId: str
        itemType: ActArchiveType
        unlockCondition: "Act13SideData.UnlockCondition"
        param1: str | None
        param2: str | None

    class ZoneAdditionData(BaseStruct):
        unlockText: str
        zoneClass: "Act13SideData.ActZoneClass"
