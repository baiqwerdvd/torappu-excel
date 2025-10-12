from pydantic import BaseModel, ConfigDict

from .special_operator_detail_const_data import SpecialOperatorDetailConstData
from .special_operator_detail_evolve_node_data import SpecialOperatorDetailEvolveNodeData
from .special_operator_detail_master_node_data import SpecialOperatorDetailMasterNodeData
from .special_operator_detail_node_unlock_data import SpecialOperatorDetailNodeUnlockData
from .special_operator_detail_skill_node_data import SpecialOperatorDetailSkillNodeData
from .special_operator_detail_tab_data import SpecialOperatorDetailTabData
from .special_operator_detail_talent_node_data import SpecialOperatorDetailTalentNodeData
from .special_operator_detail_uni_equip_node_data import SpecialOperatorDetailUniEquipNodeData
from .special_operator_diagram_data import SpecialOperatorDiagramData


class SpecialOperatorDetailData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    specialOperatorExpMap: list[list[int]]
    detailConstData: SpecialOperatorDetailConstData
    tabData: dict[str, SpecialOperatorDetailTabData]
    nodeUnlockData: dict[str, SpecialOperatorDetailNodeUnlockData]
    evolveNodeData: dict[str, SpecialOperatorDetailEvolveNodeData]
    skillNodeData: dict[str, SpecialOperatorDetailSkillNodeData]
    talentNodeData: dict[str, SpecialOperatorDetailTalentNodeData]
    masterNodeData: dict[str, SpecialOperatorDetailMasterNodeData]
    uniEquipNodeData: dict[str, SpecialOperatorDetailUniEquipNodeData]
    nodeDiagramMap: dict[str, SpecialOperatorDiagramData]
