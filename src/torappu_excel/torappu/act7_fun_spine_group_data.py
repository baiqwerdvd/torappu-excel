from .act7_fun_spine_holder_data import Act7FunSpineHolderData
from ..common import BaseStruct


class Act7FunSpineGroupData(BaseStruct):
    spineGroupId: str
    holderData: list[Act7FunSpineHolderData]
