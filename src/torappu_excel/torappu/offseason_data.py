from .offseason_const_data import OffseasonConstData
from ..common import BaseStruct


class OffseasonData(BaseStruct):
    offseasonId: str
    versionId: str
    offseasonConstData: OffseasonConstData
