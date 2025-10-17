from .common_avail_check import CommonAvailCheck
from ..common import BaseStruct


class PicGroup(BaseStruct):
    sortIndex: int
    picId: str
    availCheck: CommonAvailCheck
