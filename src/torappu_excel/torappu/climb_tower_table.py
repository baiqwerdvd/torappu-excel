from .climb_tower_curse_card_data import ClimbTowerCurseCardData
from .climb_tower_detail_const import ClimbTowerDetailConst
from .climb_tower_main_card_data import ClimbTowerMainCardData
from .climb_tower_mission_data import ClimbTowerMissionData
from .climb_tower_reward_info import ClimbTowerRewardInfo
from .climb_tower_season_info_data import ClimbTowerSeasonInfoData
from .climb_tower_single_level_data import ClimbTowerSingleLevelData
from .climb_tower_single_tower_data import ClimbTowerSingleTowerData
from .climb_tower_sub_card_data import ClimbTowerSubCardData
from .climb_tower_tactical_buff_data import ClimbTowerTacticalBuffData
from .mission_group import MissionGroup
from ..common import BaseStruct


class ClimbTowerTable(BaseStruct):
    towers: dict[str, ClimbTowerSingleTowerData]
    levels: dict[str, ClimbTowerSingleLevelData]
    tacticalBuffs: dict[str, ClimbTowerTacticalBuffData]
    mainCards: dict[str, ClimbTowerMainCardData]
    subCards: dict[str, ClimbTowerSubCardData]
    curseCards: dict[str, ClimbTowerCurseCardData]
    seasonInfos: dict[str, ClimbTowerSeasonInfoData]
    detailConst: ClimbTowerDetailConst
    rewardInfoList: list[ClimbTowerRewardInfo]
    rewardInfoListHardMode: list[ClimbTowerRewardInfo]
    missionData: dict[str, ClimbTowerMissionData]
    missionGroup: dict[str, MissionGroup]
