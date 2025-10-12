from enum import StrEnum

from pydantic import BaseModel, ConfigDict

from .item_bundle import ItemBundle
from .occ_per import OccPer
from .rune_table import RuneTable
from .stage_drop_type import StageDropType


class ActivityBossRushData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

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

    class ZoneAdditionData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        unlockText: str
        displayStartTime: int

    class BossRushStageGroupData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        stageGroupId: str
        sortId: int
        stageGroupName: str
        stageIdMap: dict["ActivityBossRushData.BossRushStageType", str]
        waveBossInfo: list[list[str]]
        normalStageCount: int
        isHardStageGroup: bool
        unlockCondtion: str | None

    class BossRushStageAdditionData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        stageId: str
        stageType: "ActivityBossRushData.BossRushStageType"
        stageGroupId: str
        teamIdList: list[str]
        unlockText: str | None

    class DisplayDetailRewards(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        occPercent: OccPer
        dropCount: int
        type: str
        id: str
        dropType: StageDropType

    class BossRushDropInfo(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        clearWaveCount: int
        displayDetailRewards: list["ActivityBossRushData.DisplayDetailRewards"]
        firstPassRewards: list[ItemBundle]
        passRewards: list[ItemBundle]

    class BossRushMissionAdditionData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        missionId: str
        isRelicTask: bool

    class BossRushTeamData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        teamId: str
        teamName: str
        charIdList: list[str]
        teamBuffName: str | None
        teamBuffDes: str | None
        teamBuffId: str | None
        maxCharNum: int
        runeData: RuneTable.PackedRuneData | None

    class RelicData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        relicId: str
        sortId: int
        name: str
        icon: str
        relicTaskId: str

    class RelicLevelInfo(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        level: int
        effectDesc: str
        runeData: RuneTable.PackedRuneData
        needItemCount: int

    class RelicLevelInfoData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        relicId: str
        levelInfos: dict[str, "ActivityBossRushData.RelicLevelInfo"]

    class BossRushMileStoneData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        mileStoneId: str
        mileStoneLvl: int
        needPointCnt: int
        rewardItem: ItemBundle

    class ConstData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        maxProvidedCharNum: int
        textMilestoneItemLevelDesc: str
        milestonePointId: str
        relicUpgradeItemId: str
        defaultRelictList: list[str]
        rewardSkinId: str
