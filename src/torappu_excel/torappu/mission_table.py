from .cross_app_share_mission import CrossAppShareMission
from .cross_app_share_mission_const import CrossAppShareMissionConst
from .daily_mission_group_info import DailyMissionGroupInfo
from .guide_mission_group_info import GuideMissionGroupInfo
from .mainline_mission_end_image_data import MainlineMissionEndImageData
from .mission_daily_reward_conf import MissionDailyRewardConf
from .mission_data import MissionData
from .mission_group import MissionGroup
from .mission_weekly_reward_conf import MissionWeeklyRewardConf
from ..common import BaseStruct

from msgspec import field


class MissionTable(BaseStruct):
    missions: dict[str, MissionData]
    missionGroups: dict[str, MissionGroup]
    periodicalRewards: dict[str, MissionDailyRewardConf]
    weeklyRewards: dict[str, MissionWeeklyRewardConf]
    dailyMissionGroupInfo: dict[str, DailyMissionGroupInfo]
    dailyMissionPeriodInfo: list[DailyMissionGroupInfo]
    mainlineMissionEndImageDataList: list[MainlineMissionEndImageData]
    crossAppShareMissions: dict[str, CrossAppShareMission] = field(default_factory=dict)
    crossAppShareMissionConst: CrossAppShareMissionConst = field(default_factory=CrossAppShareMissionConst)
    guideMissionGroupInfo: dict[str, GuideMissionGroupInfo] = field(default_factory=dict)
