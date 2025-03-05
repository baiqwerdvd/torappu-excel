from .act4fun_stage_attribute_type import Act4funStageAttributeType
from .act_4fun_live_mat_effect_info import Act4funLiveMatEffectInfo
from ..common import BaseStruct


class Act4funLiveMatInfoData(BaseStruct):
    liveMatId: str
    stageId: str
    name: str
    picId: str
    tagTxt: str
    emojiIcon: str
    selectedPerformId: str
    effectInfos: dict[Act4funStageAttributeType, Act4funLiveMatEffectInfo]
