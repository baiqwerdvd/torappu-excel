from .medal_group_data import MedalGroupData
from ..common import BaseStruct


class MedalTypeData(BaseStruct):
    medalGroupId: str
    sortId: int
    medalName: str
    groupData: list[MedalGroupData]
