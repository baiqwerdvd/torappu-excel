from .act7_fun_char_anim_data import Act7FunCharAnimData
from .act7_fun_const_data import Act7FunConstData
from .act7_fun_easter_egg_data import Act7FunEasterEggData
from .act7_fun_spine_group_data import Act7FunSpineGroupData
from .act7_fun_stage_addition_data import Act7FunStageAdditionData
from ..common import BaseStruct


class Act7FunData(BaseStruct):
    stageAdditionMap: dict[str, Act7FunStageAdditionData]
    easterEggData: dict[str, Act7FunEasterEggData]
    spineGroupData: dict[str, Act7FunSpineGroupData]
    charAnimData: dict[str, Act7FunCharAnimData]
    stageRewardList: list[str]
    constData: Act7FunConstData
