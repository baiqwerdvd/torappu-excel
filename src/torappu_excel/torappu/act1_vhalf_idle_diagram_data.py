from pydantic import BaseModel, ConfigDict

from .vector2 import Vector2


class Act1VHalfIdleDiagramData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    width: float
    height: float
    pointPosDataMap: dict[str, "Act1VHalfIdleDiagramData.PointPosData"]
    linePosDataMap: dict[str, "Act1VHalfIdleDiagramData.LinePosData"]
    lineRelationDataMap: dict[str, "Act1VHalfIdleDiagramData.LineRelationData"]
    nodePointDataMap: dict[str, "Act1VHalfIdleDiagramData.NodePointData"]

    class PointPosData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        pos: Vector2

    class LinePosData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        startPos: Vector2
        endPos: Vector2

    class LineRelationData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        startPointList: list[str]
        endPointList: list[str]

    class NodePointData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        nodeId: str
