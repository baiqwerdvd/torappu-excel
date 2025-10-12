from pydantic import BaseModel, ConfigDict

from .special_operator_detail_node_type import SpecialOperatorDetailNodeType


class SpecialOperatorDetailTabData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    soTabId: str
    soTabName: str
    soTabSortId: int
    nodeType: SpecialOperatorDetailNodeType
