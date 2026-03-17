from .return_all_open_type import ReturnAllOpenType
from ..common import BaseStruct


class ReturnOpenData(BaseStruct):
    allOpenType: ReturnAllOpenType
    allOpenTime: int
    desc: str
