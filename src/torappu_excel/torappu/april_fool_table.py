from .act_4fun_data import Act4funData
from .act_5fun_data import Act5FunData
from .april_fool_const import AprilFoolConst
from .april_fool_score_data import AprilFoolScoreData
from .april_fool_stage_data import AprilFoolStageData
from ..common import BaseStruct


class AprilFoolTable(BaseStruct):
    stages: dict[str, AprilFoolStageData]
    scoreDict: dict[str, list[AprilFoolScoreData]]
    constant: AprilFoolConst
    act4FunData: Act4funData
    act5FunData: Act5FunData
