from .special_operator_elite_point_data import SpecialOperatorElitePointData
from .special_operator_level_point_data import SpecialOperatorLevelPointData
from .special_operator_line_pos_data import SpecialOperatorLinePosData
from .special_operator_line_relation_data import SpecialOperatorLineRelationData
from .special_operator_node_point_data import SpecialOperatorNodePointData
from .special_operator_point_pos_data import SpecialOperatorPointPosData
from ..common import BaseStruct


class SpecialOperatorDiagramData(BaseStruct):
    width: float
    height: float
    pointPosDataMap: dict[str, SpecialOperatorPointPosData]
    nodePointDataMap: dict[str, SpecialOperatorNodePointData]
    elitePointDataMap: dict[str, SpecialOperatorElitePointData]
    levelPointDataMap: dict[str, SpecialOperatorLevelPointData]
    linePosDataMap: dict[str, SpecialOperatorLinePosData]
    lineRelationDataMap: dict[str, SpecialOperatorLineRelationData]
