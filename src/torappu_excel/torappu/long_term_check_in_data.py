from pydantic import BaseModel, ConfigDict

from .long_term_check_in_const_data import LongTermCheckInConstData
from .long_term_check_in_group_data import LongTermCheckInGroupData


class LongTermCheckInData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    groupList: list[LongTermCheckInGroupData]
    constData: LongTermCheckInConstData
