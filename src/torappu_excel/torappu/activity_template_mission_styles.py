from .template_mission_big_reward_type import TemplateMissionBigRewardType
from .template_mission_coin_info_type import TemplateMissionCoinInfoType
from .template_mission_title_type import TemplateMissionTitleType
from ..common import BaseStruct


class ActivityTemplateMissionStyles(BaseStruct):
    bigRewardType: TemplateMissionBigRewardType
    bigRewardParamList: list[str]
    isMissionListCommonType: bool
    isMissionItemCommonType: bool
    missionItemMainColor: str | None
    isMissionItemCompleteUseMainColor: bool
    missionItemCompleteColor: str | None
    isMissionRewardItemCommonType: bool
    isClaimAllBtnCommonType: bool
    claimAllBtnMainColor: str | None
    claimAllBtnTips: str | None
    titleType: TemplateMissionTitleType
    coinType: TemplateMissionCoinInfoType
    coinBackColor: str | None
