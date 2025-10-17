from .special_operator_detail_node_type import SpecialOperatorDetailNodeType
from ..common import BaseStruct


class SpecialOperatorDetailTabData(BaseStruct):
    soTabId: str
    soTabName: str
    soTabSortId: int
    nodeType: SpecialOperatorDetailNodeType
