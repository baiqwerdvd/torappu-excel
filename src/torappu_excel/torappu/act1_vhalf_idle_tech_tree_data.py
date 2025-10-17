from .act1_vhalf_idle_tech_tree_node_type import Act1VHalfIdleTechTreeNodeType
from .rune_table import RuneTable
from ..common import BaseStruct


class Act1VHalfIdleTechTreeData(BaseStruct):
    nodeId: str
    nodeType: Act1VHalfIdleTechTreeNodeType
    prevNodeId: list[str] | None
    tokenCost: int
    name: str
    iconId: str
    showPrevLockTips: bool
    effect: list["Act1VHalfIdleTechTreeData.Effect"]

    class Effect(BaseStruct):
        desc: str
        title: str
        iconId: str
        runeDatas: list["RuneTable.PackedRuneData"] | None
