from .act_4fun_cmt_group_info import Act4funCmtGroupInfo
from .act_4fun_const import Act4funConst
from .act_4fun_ending_info import Act4funEndingInfo
from .act_4fun_live_mat_info_data import Act4funLiveMatInfoData
from .act_4fun_live_value_info_data import Act4funLiveValueInfoData
from .act_4fun_mission_data import Act4funMissionData
from .act_4fun_perform_group_info import Act4funPerformGroupInfo
from .act_4fun_perform_info import Act4funPerformInfo
from .act_4fun_sp_live_mat_info_data import Act4funSpLiveMatInfoData
from .act_4fun_stage_extra_data import Act4funStageExtraData
from .act_4fun_super_chat_info import Act4funSuperChatInfo
from .act_4fun_token_info_data import Act4funTokenInfoData
from .act_4fun_value_effect_info_data import Act4funValueEffectInfoData
from ..common import BaseStruct


class Act4funData(BaseStruct):
    performGroupInfoDict: dict[str, Act4funPerformGroupInfo]
    performInfoDict: dict[str, Act4funPerformInfo]
    normalMatDict: dict[str, Act4funLiveMatInfoData]
    spMatDict: dict[str, Act4funSpLiveMatInfoData]
    valueEffectInfoDict: dict[str, Act4funValueEffectInfoData]
    liveValueInfoDict: dict[str, Act4funLiveValueInfoData]
    superChatInfoDict: dict[str, Act4funSuperChatInfo]
    cmtGroupInfoDict: dict[str, Act4funCmtGroupInfo]
    cmtUsers: list[str]
    endingDict: dict[str, Act4funEndingInfo]
    tokenLevelInfos: dict[str, Act4funTokenInfoData]
    missionDatas: dict[str, Act4funMissionData]
    constant: Act4funConst
    stageExtraDatas: dict[str, Act4funStageExtraData]
    randomMsgText: list[str]
    randomUserIconId: list[str]
