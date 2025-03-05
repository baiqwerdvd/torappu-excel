from typing import Any

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
from .act_mainline_bp_extra_data import ActMainlineBpExtraData
from .act_sandbox_data import ActSandboxData
from .act_vec_break_data import ActVecBreakData
from .activity_auto_chess_verify1_data import ActivityAutoChessVerify1Data
from .activity_boss_rush_data import ActivityBossRushData
from .activity_collection_data import ActivityCollectionData
from .activity_complete_type import ActivityCompleteType
from .activity_display_type import ActivityDisplayType
from .activity_dyn_entry_switch_data import ActivityDynEntrySwitchData
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
from .mission_archive_data import MissionArchiveData
from .mission_data import MissionData
from .mission_display_rewards import MissionDisplayRewards
from .mission_group import MissionGroup
from .mission_type import MissionType
from .rune_table import RuneTable
from .siracusa_data import SiracusaData
from .versus_checkin_data import VersusCheckInData
from ..common import BaseStruct

from msgspec import field


class ActivityTable(BaseStruct):
    basicInfo: dict[str, "ActivityTable.BasicData"]
    homeActConfig: dict[str, "ActivityTable.HomeActivityConfig"]
    zoneToActivity: dict[str, str]
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

    class BasicData(BaseStruct):
        id_: str = field(name="id")
        type_: ActivityType = field(name="type")
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
        trapDomainId: str | None = field(default=None)
        displayType: ActivityDisplayType | None = field(default=None)
        recType: ActivityCompleteType | None = field(default=None)
        ungroupedMedalIds: list[str] | None = field(default=None)

    class HomeActivityConfig(BaseStruct):
        actId: str
        isPopupAfterCheckin: bool
        showTopBarMenu: bool
        actTopBarColor: str | None
        actTopBarText: str | None

    class ActivityDetailTable(BaseStruct):
        DEFAULT: dict[str, "DefaultFirstData"] = field(default_factory=dict)
        CHECKIN_ONLY: dict[str, "DefaultCheckInData"] = field(default_factory=dict)
        CHECKIN_ALL_PLAYER: dict[str, "AllPlayerCheckinData"] = field(default_factory=dict)
        CHECKIN_VS: dict[str, "VersusCheckInData"] = field(default_factory=dict)
        TYPE_ACT3D0: dict[str, "Act3D0Data"] = field(default_factory=dict)
        TYPE_ACT4D0: dict[str, "Act4D0Data"] = field(default_factory=dict)
        TYPE_ACT5D0: dict[str, "Act5D0Data"] = field(default_factory=dict)
        TYPE_ACT5D1: dict[str, "Act5D1Data"] = field(default_factory=dict)
        COLLECTION: dict[str, "ActivityCollectionData"] = field(default_factory=dict)
        TYPE_ACT9D0: dict[str, "Act9D0Data"] = field(default_factory=dict)
        TYPE_ACT12SIDE: dict[str, "Act12SideData"] = field(default_factory=dict)
        TYPE_ACT13SIDE: dict[str, "Act13SideData"] = field(default_factory=dict)
        TYPE_ACT17SIDE: dict[str, "Act17sideData"] = field(default_factory=dict)
        TYPE_ACT20SIDE: dict[str, "Act20SideData"] = field(default_factory=dict)
        TYPE_ACT21SIDE: dict[str, "Act21SideData"] = field(default_factory=dict)
        LOGIN_ONLY: dict[str, "ActivityLoginData"] = field(default_factory=dict)
        SWITCH_ONLY: dict[str, "ActivitySwitchCheckinData"] = field(default_factory=dict)
        MINISTORY: dict[str, "ActivityMiniStoryData"] = field(default_factory=dict)
        ROGUELIKE: dict[str, "ActivityRoguelikeData"] = field(default_factory=dict)
        MULTIPLAY: dict[str, "ActivityMultiplayData"] = field(default_factory=dict)
        MULTIPLAY_VERIFY2: dict[str, "ActivityMultiplayVerify2Data"] = field(default_factory=dict)
        INTERLOCK: dict[str, "ActivityInterlockData"] = field(default_factory=dict)
        BOSS_RUSH: dict[str, "ActivityBossRushData"] = field(default_factory=dict)
        FLOAT_PARADE: dict[str, "ActivityFloatParadeData"] = field(default_factory=dict)
        SANDBOX: dict[str, "ActSandboxData"] = field(default_factory=dict)
        MAIN_BUFF: dict[str, "ActivityMainlineBuffData"] = field(default_factory=dict)
        TYPE_ACT24SIDE: dict[str, "Act24SideData"] = field(default_factory=dict)
        TYPE_ACT25SIDE: dict[str, "Act25SideData"] = field(default_factory=dict)
        TYPE_ACT27SIDE: dict[str, "Act27SideData"] = field(default_factory=dict)
        TYPE_ACT38D1: dict[str, "Act38D1Data"] = field(default_factory=dict)
        TYPE_ACT42D0: dict[str, "Act42D0Data"] = field(default_factory=dict)
        TYPE_ACT29SIDE: dict[str, "Act29SideData"] = field(default_factory=dict)
        YEAR_5_GENERAL: dict[str, "ActivityYear5GeneralData"] = field(default_factory=dict)
        TYPE_ACT35SIDE: dict[str, "Act35SideData"] = field(default_factory=dict)
        VEC_BREAK: dict[str, "ActVecBreakData"] = field(default_factory=dict)
        TYPE_ACT36SIDE: dict[str, "Act36SideData"] = field(default_factory=dict)
        TYPE_ACT38SIDE: dict[str, "Act38SideData"] = field(default_factory=dict)
        AUTOCHESS_VERIFY1: dict[str, "ActivityAutoChessVerify1Data"] = field(default_factory=dict)
        ARCADE: dict[str, "ActArcadeData"] = field(default_factory=dict)

    class ActivityExtraData(BaseStruct):
        MAINLINE_BP: dict[str, "ActMainlineBpExtraData"]

    class ActivityHiddenStageUnlockConditionData(BaseStruct):
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

    class ActivityHiddenStageData(BaseStruct):
        stageId: str
        encodedName: str
        showStageId: str
        rewardDiamond: bool
        missions: list["ActivityTable.ActivityHiddenStageUnlockConditionData"]

    class ExtraData(BaseStruct):
        periodId: str
        startTs: int
        endTs: int

    class TemplateTrapData(BaseStruct):
        trapId: str
        sortId: int
        trapName: str
        trapDesc: str
        trapText: str
        trapTaskId: str
        trapUnlockDesc: str
        trapBuffId: str

    class ActivityTrapConstData(BaseStruct):
        stageUnlockTrapDesc: str
        trapMaximum: int
        stageCanNotUseTrap: list[str]

    class ActivityTrapsData(BaseStruct):
        templateTraps: dict[str, "ActivityTable.TemplateTrapData"]
        trapConstData: "ActivityTable.ActivityTrapConstData"

    class TrapMissionData(BaseStruct):
        id_: str = field(name="id")
        description: str
        type_: MissionType = field(name="type")
        rewards: list["MissionDisplayRewards"]

    class ActivityTrapMissionsData(BaseStruct):
        trapMissions: dict[str, "ActivityTable.TrapMissionData"]
