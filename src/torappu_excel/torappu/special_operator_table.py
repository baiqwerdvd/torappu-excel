from .mission_data import MissionData
from .mission_group import MissionGroup
from .special_operator_basic_data import SpecialOperatorBasicData
from .special_operator_const_data import SpecialOperatorConstData
from .special_operator_detail_data import SpecialOperatorDetailData
from .special_operator_mode_data import SpecialOperatorModeData
from ..common import BaseStruct


class SpecialOperatorTable(BaseStruct):
    operatorBasicData: dict[str, SpecialOperatorBasicData]
    operatorDetailData: dict[str, SpecialOperatorDetailData]
    modeData: list[SpecialOperatorModeData]
    nodeUnlockMissionData: dict[str, MissionData]
    nodeUnlockMissionGroup: dict[str, MissionGroup]
    constData: SpecialOperatorConstData
