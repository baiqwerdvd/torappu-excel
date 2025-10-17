from .item_bundle import ItemBundle
from .rune_table import RuneTable
from ..common import BaseStruct, CustomIntEnum


class ActArcadeData(BaseStruct):
    class Rank(CustomIntEnum):
        B = "B", 0
        A = "A", 1
        S = "S", 2
        SS = "SS", 3
        SSS = "SSS", 4

    class BadgeType(CustomIntEnum):
        COMMON = "COMMON", 0
        ZONE = "ZONE", 1
        ULTIMATE = "ULTIMATE", 2

    class SubModeType(CustomIntEnum):
        MINER = "MINER", 0
        DRAW = "DRAW", 1
        LINE = "LINE", 2
        CAR = "CAR", 3
        E_NUM = "E_NUM", 4
        IGNORE = "IGNORE", -1

    stageAdditionDataDict: dict[str, "ActArcadeData.ArcadeStageAdditionalData"]
    zoneAdditionalDataDict: dict[str, "ActArcadeData.ArcadeZoneAdditionalData"]
    badgeDataDict: dict[str, "ActArcadeData.ArcadeBadgeData"]
    tireBadgeIdDict: dict[str, str]
    badgeTypeDataDict: dict[str, "ActArcadeData.ArcadeBadgeTypeData"]
    milestoneList: list["ActArcadeData.ArcadeMilestoneItemData"]
    constData: "ActArcadeData.ArcadeConstData"

    class ArcadeStageRankRewardLevelData(BaseStruct):
        rank: "ActArcadeData.Rank"
        rankScore: int
        coinCnt: int

    class ArcadeStageRankRewardData(BaseStruct):
        stageId: str
        maxRewardRank: "ActArcadeData.Rank"
        rankRewardLevelDatas: list["ActArcadeData.ArcadeStageRankRewardLevelData"]

    class ArcadeStageAdditionalData(BaseStruct):
        stageId: str
        zoneId: str
        mechDescription: str
        sortId: int
        maxSlot: int
        rankRewardData: "ActArcadeData.ArcadeStageRankRewardData"

    class ArcadeZoneAdditionalData(BaseStruct):
        zoneId: str
        sortId: int
        zoneName: str
        zoneEntryPicId: str
        stageInfoPrefabId: str
        startTs: int
        endTs: int
        stages: list[str]
        subModeType: "ActArcadeData.SubModeType"
        zoneDesc: str

    class ArcadeBadgeTierData(BaseStruct):
        badgeTierId: str
        sortId: int
        badgeTierIconId: str
        badgeTierShareIconId: str
        badgeTierEffectId: str | None
        title: str
        desc: str
        buffId: str
        unlockDesc: str
        runeData: RuneTable.PackedRuneData | None

    class ArcadeBadgeData(BaseStruct):
        badgeId: str
        badgeType: "ActArcadeData.BadgeType"
        sortId: int
        badgeName: str
        buffRangeDesc: str | None
        hasScore: bool
        scoreZone: str | None
        tiers: dict[str, "ActArcadeData.ArcadeBadgeTierData"]

    class ArcadeBadgeTypeData(BaseStruct):
        badgeType: "ActArcadeData.BadgeType"
        badgeTypeName: str
        sortId: int
        buffRangeDesc: str | None

    class ArcadeMilestoneItemData(BaseStruct):
        mileStoneId: str
        mileStoneLvl: int
        needPointCnt: int
        reward: ItemBundle

    class ArcadeConstData(BaseStruct):
        milestoneName: str
        milestoneNameEN: str
        milestoneItemId: str
        rewardHomeThemeId: str
        rewardHomeThemeText: str
        rewardAvatarId: str
        rewardAvatarText: str
        badgeCollectionName: str
        collectionEntryRelatedBadge: str
        zoneEntryUnlockToast: str
        zoneEntryEndText: str
        zoneEntryEndToast: str
        rankUnlockNextStage: str
        stageScoreDisplayLimit: int
        zoneUltiScoreDisplayLimit: int
        enemyHudScore: list[str]
        trapNotBuildableInRest: list[str]
