from pydantic import BaseModel, ConfigDict

from .evolve_phase import EvolvePhase
from .special_operator_condition_view_type import SpecialOperatorConditionViewType
from .special_operator_detail_node_type import SpecialOperatorDetailNodeType


class SpecialOperatorDetailNodeUnlockData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    nodeId: str
    nodeType: SpecialOperatorDetailNodeType
    isInGameMechanics: bool
    unlockEvolvePhase: EvolvePhase
    unlockLevel: int
    unlockTaskId: str | None
    frontNodeId: str | None
    ifAutoUnlock: bool
    conditionViewType: SpecialOperatorConditionViewType
    topoOrder: int
