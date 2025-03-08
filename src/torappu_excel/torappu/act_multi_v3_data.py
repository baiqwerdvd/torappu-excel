from .act_multi_v3_const_data import ActMultiV3ConstData
from .act_multi_v3_const_toast_data import ActMultiV3ConstToastData
from .act_multi_v3_diff_star_reward_data import ActMultiV3DiffStarRewardData
from .act_multi_v3_identity_data import ActMultiV3IdentityData
from .act_multi_v3_map_data import ActMultiV3MapData
from .act_multi_v3_map_diff_data import ActMultiV3MapDiffData
from .act_multi_v3_map_mode_data import ActMultiV3MapModeData
from .act_multi_v3_map_type_data import ActMultiV3MapTypeData
from .act_multi_v3_match_pos_data import ActMultiV3MatchPosData
from .act_multi_v3_milestone_data import ActMultiV3MilestoneData
from .act_multi_v3_photo_type_data import ActMultiV3PhotoTypeData
from .act_multi_v3_report_data import ActMultiV3ReportData
from .act_multi_v3_select_step_data import ActMultiV3SelectStepData
from .act_multi_v3_squad_effect_data import ActMultiV3SquadEffectData
from .act_multi_v3_squad_info_data import ActMultiV3SquadInfoData
from .act_multi_v3_target_mission_data import ActMultiV3TargetMissionData
from .act_multi_v3_temp_char_data import ActMultiV3TempCharData
from .act_multi_v3_tips_data import ActMultiV3TipsData
from .act_multi_v3_title_data import ActMultiV3TitleData
from .act_multi_v3_weekly_photo_reward_data import ActMultiV3WeeklyPhotoRewardData
from ..common import BaseStruct


class ActMultiV3Data(BaseStruct):
    selectStepDataList: list[ActMultiV3SelectStepData]
    squadInfoList: list[ActMultiV3SquadInfoData]
    identityDataList: list[ActMultiV3IdentityData]
    squadEffectList: list[ActMultiV3SquadEffectData]
    targetMissionDataDict: dict[str, ActMultiV3TargetMissionData]
    mapTypeDataDict: dict[str, ActMultiV3MapTypeData]
    mapDataDict: dict[str, ActMultiV3MapData]
    mapModeDataDict: dict[str, ActMultiV3MapModeData]
    mapDiffDataDict: dict[str, ActMultiV3MapDiffData]
    missionTitleDict: dict[str, str]
    titleDataDict: dict[str, ActMultiV3TitleData]
    photoTypeDataDict: dict[str, ActMultiV3PhotoTypeData]
    photoWeeklyRewardDataDict: dict[str, ActMultiV3WeeklyPhotoRewardData]
    matchPosDataDict: dict[str, ActMultiV3MatchPosData]
    enabledEmoticonThemeIdList: list[str]
    diffStarRewardDict: dict[str, ActMultiV3DiffStarRewardData]
    milestoneList: list[ActMultiV3MilestoneData]
    tipsDataList: list[ActMultiV3TipsData]
    reportDataList: list[ActMultiV3ReportData]
    tempCharDataList: list[ActMultiV3TempCharData]
    constToastData: ActMultiV3ConstToastData
    constData: ActMultiV3ConstData
