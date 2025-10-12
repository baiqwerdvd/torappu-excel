from pydantic import BaseModel, ConfigDict

from .act1_vhalf_idle_tech_tree_node_type import Act1VHalfIdleTechTreeNodeType
from .rune_table import RuneTable


class Act1VHalfIdleTechTreeData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    nodeId: str
    nodeType: Act1VHalfIdleTechTreeNodeType
    prevNodeId: list[str] | None
    tokenCost: int
    name: str
    iconId: str
    showPrevLockTips: bool
    effect: list["Act1VHalfIdleTechTreeData.Effect"]

    class Effect(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        desc: str
        title: str
        iconId: str
        runeDatas: list["RuneTable.PackedRuneData"] | None
