from enum import StrEnum

from .item_bundle import ItemBundle
from .occ_per import OccPer
from .rune_table import RuneTable
from .stage_drop_type import StageDropType
from ..common import BaseStruct

from msgspec import field


class ActivityBossRushData(BaseStruct):
    class BossRushStageType(StrEnum):
        NONE = "NONE"
        NORMAL = "NORMAL"
        TEAM = "TEAM"
        EX = "EX"
        SP = "SP"

    class BossRushPrincipleDialogType(StrEnum):
        NONE = "NONE"

    zoneAdditionDataMap: dict[str, "ActivityBossRushData.ZoneAdditionData"]
    stageGroupMap: dict[str, "ActivityBossRushData.BossRushStageGroupData"]
    stageAdditionDataMap: dict[str, "ActivityBossRushData.BossRushStageAdditionData"]
    stageDropDataMap: dict[str, dict[str, "ActivityBossRushData.BossRushDropInfo"]]
    missionAdditionDataMap: dict[str, "ActivityBossRushData.BossRushMissionAdditionData"]
    teamDataMap: dict[str, "ActivityBossRushData.BossRushTeamData"]
    relicList: list["ActivityBossRushData.RelicData"]
    relicLevelInfoDataMap: dict[str, "ActivityBossRushData.RelicLevelInfoData"]
    mileStoneList: list["ActivityBossRushData.BossRushMileStoneData"]
    bestWaveRuneList: list[RuneTable.PackedRuneData]
    constData: "ActivityBossRushData.ConstData"

    class ZoneAdditionData(BaseStruct):
        unlockText: str
        displayStartTime: int

    class BossRushStageGroupData(BaseStruct):
        stageGroupId: str
        sortId: int
        stageGroupName: str
        stageIdMap: dict["ActivityBossRushData.BossRushStageType", str]
        waveBossInfo: list[list[str]]
        normalStageCount: int
        isHardStageGroup: bool
        unlockCondtion: str | None

    class BossRushStageAdditionData(BaseStruct):
        stageId: str
        stageType: "ActivityBossRushData.BossRushStageType"
        stageGroupId: str
        teamIdList: list[str]
        unlockText: str | None

    class DisplayDetailRewards(BaseStruct):
        occPercent: OccPer
        dropCount: int
        type_: str = field(name="type")
        id_: str = field(name="id")
        dropType: StageDropType

    class BossRushDropInfo(BaseStruct):
        clearWaveCount: int
        displayDetailRewards: list["ActivityBossRushData.DisplayDetailRewards"]
        firstPassRewards: list[ItemBundle]
        passRewards: list[ItemBundle]

    class BossRushMissionAdditionData(BaseStruct):
        missionId: str
        isRelicTask: bool

    class BossRushTeamData(BaseStruct):
        teamId: str
        teamName: str
        charIdList: list[str]
        teamBuffName: str | None
        teamBuffDes: str | None
        teamBuffId: str | None
        maxCharNum: int
        runeData: RuneTable.PackedRuneData | None

    class RelicData(BaseStruct):
        relicId: str
        sortId: int
        name: str
        icon: str
        relicTaskId: str

    class RelicLevelInfo(BaseStruct):
        level: int
        effectDesc: str
        runeData: RuneTable.PackedRuneData
        needItemCount: int

    class RelicLevelInfoData(BaseStruct):
        relicId: str
        levelInfos: dict[str, "ActivityBossRushData.RelicLevelInfo"]

    class BossRushMileStoneData(BaseStruct):
        mileStoneId: str
        mileStoneLvl: int
        needPointCnt: int
        rewardItem: ItemBundle

    class ConstData(BaseStruct):
        maxProvidedCharNum: int
        textMilestoneItemLevelDesc: str
        milestonePointId: str
        relicUpgradeItemId: str
        defaultRelictList: list[str]
        rewardSkinId: str
