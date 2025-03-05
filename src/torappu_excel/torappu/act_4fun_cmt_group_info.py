from .act_4fun_cmt_info import Act4funCmtInfo
from ..common import BaseStruct


class Act4funCmtGroupInfo(BaseStruct):
    cmtGroupId: str
    cmtList: list[Act4funCmtInfo]
