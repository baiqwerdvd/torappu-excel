from .vector2 import Vector2
from ..common import BaseStruct


class Act1VHalfIdleDiagramData(BaseStruct):
    width: float
    height: float
    pointPosDataMap: dict[str, "Act1VHalfIdleDiagramData.PointPosData"]
    linePosDataMap: dict[str, "Act1VHalfIdleDiagramData.LinePosData"]
    lineRelationDataMap: dict[str, "Act1VHalfIdleDiagramData.LineRelationData"]
    nodePointDataMap: dict[str, "Act1VHalfIdleDiagramData.NodePointData"]

    class PointPosData(BaseStruct):
        pos: Vector2

    class LinePosData(BaseStruct):
        startPos: Vector2
        endPos: Vector2

    class LineRelationData(BaseStruct):
        startPointList: list[str]
        endPointList: list[str]

    class NodePointData(BaseStruct):
        nodeId: str
