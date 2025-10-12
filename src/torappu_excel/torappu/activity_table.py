from typing import Any

from pydantic import BaseModel, ConfigDict, Field

from .act1_vhalf_idle_data import Act1VHalfIdleData
from .act42_side_data import Act42SideData
from .act44_side_data import Act44SideData
from .act45_side_data import Act45SideData
from .act_3d0_data import Act3D0Data
from .act_4d0_data import Act4D0Data
from .act_5d0_data import Act5D0Data
from .act_5d1_data import Act5D1Data
from .act_9d0_data import Act9D0Data
from .act_12side_data import Act12SideData
from .act_13side_data import Act13SideData
from .act_17side_data import Act17sideData
from .act_20side_data import Act20SideData
from .act_21side_data import Act21SideData
from .act_24side_data import Act24SideData
from .act_25side_data import Act25SideData
from .act_27side_data import Act27SideData
from .act_29side_data import Act29SideData
from .act_35side_data import Act35SideData
from .act_36side_data import Act36SideData
from .act_38_side_data import Act38SideData
from .act_38d1_data import Act38D1Data
from .act_42d0_data import Act42D0Data
from .act_arcade_data import ActArcadeData
from .act_main_ssdata import ActMainSSData
from .act_mainline_bp_extra_data import ActMainlineBpExtraData
from .act_multi_v3_data import ActMultiV3Data
from .act_recruit_only_data import ActRecruitOnlyData
from .act_sandbox_data import ActSandboxData
from .act_vec_break_data import ActVecBreakData
from .act_vec_break_v2_data import ActVecBreakV2Data
from .activity_auto_chess_verify1_data import ActivityAutoChessVerify1Data
from .activity_boss_rush_data import ActivityBossRushData
from .activity_collection_data import ActivityCollectionData
from .activity_complete_type import ActivityCompleteType
from .activity_display_type import ActivityDisplayType
from .activity_dyn_entry_switch_data import ActivityDynEntrySwitchData
from .activity_enemy_duel_data import ActivityEnemyDuelData
from .activity_float_parade_data import ActivityFloatParadeData
from .activity_interlock_data import ActivityInterlockData
from .activity_kv_switch_data import ActivityKVSwitchData
from .activity_login_data import ActivityLoginData
from .activity_mainline_buff_data import ActivityMainlineBuffData
from .activity_mini_story_data import ActivityMiniStoryData
from .activity_multiplay_data import ActivityMultiplayData
from .activity_multiplay_verify2_data import ActivityMultiplayVerify2Data
from .activity_roguelike_data import ActivityRoguelikeData
from .activity_stage_reward_data import ActivityStageRewardData
from .activity_switch_checkin_data import ActivitySwitchCheckinData
from .activity_template_mission_styles import ActivityTemplateMissionStyles
from .activity_theme_data import ActivityThemeData
from .activity_type import ActivityType
from .activity_year5_general_data import ActivityYear5GeneralData
from .all_player_checkin_data import AllPlayerCheckinData
from .april_fool_table import AprilFoolTable
from .cart_data import CartData
from .cross_day_track_type_data import CrossDayTrackTypeData
from .default_checkin_data import DefaultCheckInData
from .default_first_data import DefaultFirstData
from .fifth_anniv_explore_data import FifthAnnivExploreData
from .firework_data import FireworkData
from .half_idle_data import HalfIdleData
from .mission_archive_data import MissionArchiveData
from .mission_data import MissionData
from .mission_display_rewards import MissionDisplayRewards
from .mission_group import MissionGroup
from .mission_type import MissionType
from .pic_group import PicGroup
from .rune_table import RuneTable
from .siracusa_data import SiracusaData
from .versus_checkin_data import VersusCheckInData


class ActivityTable(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    basicInfo: dict[str, "ActivityTable.BasicData"]
    homeActConfig: dict[str, "ActivityTable.HomeActivityConfig"]
    zoneToActivity: dict[str, str]
    actTimeTrackPoint: dict[str, int]
    missionData: list[MissionData]
    missionGroup: list[MissionGroup]
    replicateMissions: dict[str, str] | None
    activity: "ActivityTable.ActivityDetailTable"
    extraData: "ActivityTable.ActivityExtraData"
    activityItems: dict[str, list[str]]
    syncPoints: dict[str, list[int]]
    dynActs: Any
    stageRewardsData: dict[str, ActivityStageRewardData]
    actThemes: list[ActivityThemeData]
    actFunData: AprilFoolTable
    carData: CartData
    siracusaData: SiracusaData
    fireworkData: FireworkData
    halfIdleData: HalfIdleData
    kvSwitchData: dict[str, ActivityKVSwitchData]
    dynEntrySwitchData: dict[str, ActivityDynEntrySwitchData]
    hiddenStageData: list["ActivityTable.ActivityHiddenStageData"]
    stringRes: dict[str, dict[str, str]]
    activityTraps: dict[str, "ActivityTable.ActivityTrapsData"]
    activityTrapMissions: dict[str, "ActivityTable.ActivityTrapMissionsData"]
    trapRuneDataDict: dict[str, RuneTable.PackedRuneData]
    missionArchives: dict[str, MissionArchiveData]
    fifthAnnivExploreData: FifthAnnivExploreData
    activityTemplateMissionStyles: dict[str, ActivityTemplateMissionStyles]
    activityCrossDayTrackTypeDataDict: dict[str, CrossDayTrackTypeData]
    activityCrossDayTrackTypeMap: dict[str, list[str]]

    class BasicData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        id: str
        type: ActivityType
        name: str
        startTime: int
        endTime: int
        rewardEndTime: int
        displayOnHome: bool
        hasStage: bool
        isPageEntry: bool
        templateShopId: str | None
        medalGroupId: str | None
        isReplicate: bool
        needFixedSync: bool
        isMagnify: bool
        picGroup: list[PicGroup]
        usePicGroup: bool
        trapDomainId: str | None = Field(default=None)
        displayType: ActivityDisplayType | None = Field(default=None)
        recType: ActivityCompleteType | None = Field(default=None)
        ungroupedMedalIds: list[str] | None = Field(default=None)

    class HomeActivityConfig(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        actId: str
        isPopupAfterCheckin: bool
        showTopBarMenu: bool
        actTopBarColor: str | None
        actTopBarText: str | None

    class ActivityDetailTable(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        DEFAULT: dict[str, "DefaultFirstData"] = Field(default_factory=dict[str, "DefaultFirstData"])
        CHECKIN_ONLY: dict[str, "DefaultCheckInData"] = Field(default_factory=dict)
        CHECKIN_ALL_PLAYER: dict[str, "AllPlayerCheckinData"] = Field(default_factory=dict)
        CHECKIN_VS: dict[str, "VersusCheckInData"] = Field(default_factory=dict)
        TYPE_ACT3D0: dict[str, "Act3D0Data"] = Field(default_factory=dict)
        TYPE_ACT4D0: dict[str, "Act4D0Data"] = Field(default_factory=dict)
        TYPE_ACT5D0: dict[str, "Act5D0Data"] = Field(default_factory=dict)
        TYPE_ACT5D1: dict[str, "Act5D1Data"] = Field(default_factory=dict)
        COLLECTION: dict[str, "ActivityCollectionData"] = Field(default_factory=dict)
        TYPE_ACT9D0: dict[str, "Act9D0Data"] = Field(default_factory=dict)
        TYPE_ACT12SIDE: dict[str, "Act12SideData"] = Field(default_factory=dict)
        TYPE_ACT13SIDE: dict[str, "Act13SideData"] = Field(default_factory=dict)
        TYPE_ACT17SIDE: dict[str, "Act17sideData"] = Field(default_factory=dict)
        TYPE_ACT20SIDE: dict[str, "Act20SideData"] = Field(default_factory=dict)
        TYPE_ACT21SIDE: dict[str, "Act21SideData"] = Field(default_factory=dict)
        LOGIN_ONLY: dict[str, "ActivityLoginData"] = Field(default_factory=dict)
        SWITCH_ONLY: dict[str, "ActivitySwitchCheckinData"] = Field(default_factory=dict)
        MINISTORY: dict[str, "ActivityMiniStoryData"] = Field(default_factory=dict)
        ROGUELIKE: dict[str, "ActivityRoguelikeData"] = Field(default_factory=dict)
        MULTIPLAY: dict[str, "ActivityMultiplayData"] = Field(default_factory=dict)
        MULTIPLAY_VERIFY2: dict[str, "ActivityMultiplayVerify2Data"] = Field(default_factory=dict)
        INTERLOCK: dict[str, "ActivityInterlockData"] = Field(default_factory=dict)
        BOSS_RUSH: dict[str, "ActivityBossRushData"] = Field(default_factory=dict)
        FLOAT_PARADE: dict[str, "ActivityFloatParadeData"] = Field(default_factory=dict)
        SANDBOX: dict[str, "ActSandboxData"] = Field(default_factory=dict)
        MAIN_BUFF: dict[str, "ActivityMainlineBuffData"] = Field(default_factory=dict)
        TYPE_ACT24SIDE: dict[str, "Act24SideData"] = Field(default_factory=dict)
        TYPE_ACT25SIDE: dict[str, "Act25SideData"] = Field(default_factory=dict)
        TYPE_ACT27SIDE: dict[str, "Act27SideData"] = Field(default_factory=dict)
        TYPE_ACT38D1: dict[str, "Act38D1Data"] = Field(default_factory=dict)
        TYPE_ACT42D0: dict[str, "Act42D0Data"] = Field(default_factory=dict)
        TYPE_ACT29SIDE: dict[str, "Act29SideData"] = Field(default_factory=dict)
        YEAR_5_GENERAL: dict[str, "ActivityYear5GeneralData"] = Field(default_factory=dict)
        TYPE_ACT35SIDE: dict[str, "Act35SideData"] = Field(default_factory=dict)
        VEC_BREAK: dict[str, "ActVecBreakData"] = Field(default_factory=dict)
        VEC_BREAK_V2: dict[str, "ActVecBreakV2Data"] = Field(default_factory=dict)
        TYPE_ACT36SIDE: dict[str, "Act36SideData"] = Field(default_factory=dict)
        TYPE_ACT38SIDE: dict[str, "Act38SideData"] = Field(default_factory=dict)
        AUTOCHESS_VERIFY1: dict[str, "ActivityAutoChessVerify1Data"] = Field(default_factory=dict)
        ARCADE: dict[str, "ActArcadeData"] = Field(default_factory=dict)
        MULTIPLAY_V3: dict[str, "ActMultiV3Data"] = Field(default_factory=dict)
        TYPE_MAINSS: dict[str, "ActMainSSData"] = Field(default_factory=dict)
        ENEMY_DUEL: dict[str, "ActivityEnemyDuelData"] = Field(default_factory=dict)
        TYPE_ACT42SIDE: dict[str, "Act42SideData"] = Field(default_factory=dict)
        TYPE_ACT44SIDE: dict[str, "Act44SideData"] = Field(default_factory=dict)
        HALFIDLE_VERIFY1: dict[str, "Act1VHalfIdleData"] = Field(default_factory=dict)
        TYPE_ACT45SIDE: dict[str, "Act45SideData"] = Field(default_factory=dict)
        RECRUIT_ONLY: dict[str, "ActRecruitOnlyData"] = Field(default_factory=dict)

    class ActivityExtraData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        MAINLINE_BP: dict[str, "ActMainlineBpExtraData"]

    class ActivityHiddenStageUnlockConditionData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        unlockStageId: str
        unlockTemplate: str
        unlockParams: list[str] | None
        missionStageId: str
        unlockedName: str
        lockedName: str
        lockCode: str
        unlockedDes: str
        templateDesc: str
        desc: str
        riddle: str

    class ActivityHiddenStageData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        stageId: str
        encodedName: str
        showStageId: str
        rewardDiamond: bool
        missions: list["ActivityTable.ActivityHiddenStageUnlockConditionData"]

    class ExtraData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        periodId: str
        startTs: int
        endTs: int

    class TemplateTrapData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        trapId: str
        sortId: int
        trapName: str
        trapDesc: str
        trapText: str
        trapTaskId: str
        trapUnlockDesc: str
        trapBuffId: str

    class ActivityTrapConstData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        stageUnlockTrapDesc: str
        trapMaximum: int
        stageCanNotUseTrap: list[str]

    class ActivityTrapsData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        templateTraps: dict[str, "ActivityTable.TemplateTrapData"]
        trapConstData: "ActivityTable.ActivityTrapConstData"

    class TrapMissionData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        id: str
        description: str
        type: MissionType
        rewards: list["MissionDisplayRewards"]

    class ActivityTrapMissionsData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        trapMissions: dict[str, "ActivityTable.TrapMissionData"]
