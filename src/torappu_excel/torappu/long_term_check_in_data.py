from .long_term_check_in_const_data import LongTermCheckInConstData
from .long_term_check_in_group_data import LongTermCheckInGroupData
from ..common import BaseStruct


class LongTermCheckInData(BaseStruct):
    groupList: list[LongTermCheckInGroupData]
    constData: LongTermCheckInConstData
