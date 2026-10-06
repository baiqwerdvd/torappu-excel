from .anniv7th_display_data import Anniv7thDisplayData
from .anniv7th_display_node_type import Anniv7thDisplayNodeType
from ..common import BaseStruct


class Anniv7thDisplayNodeData(BaseStruct):
    nodeType: Anniv7thDisplayNodeType
    displayData: list[Anniv7thDisplayData]
