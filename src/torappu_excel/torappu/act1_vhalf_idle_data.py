from pydantic import BaseModel, ConfigDict

from .act1_vbattle_item_drop_slot import Act1VBattleItemDropSlot
from .act1_vhalf_idle_char_buff_data import Act1VHalfIdleCharBuffData
from .act1_vhalf_idle_char_evolve_data import Act1VHalfIdleCharEvolveData
from .act1_vhalf_idle_char_max_rank_data import Act1VHalfIdleCharMaxRankData
from .act1_vhalf_idle_char_rank_data import Act1VHalfIdleCharRankData
from .act1_vhalf_idle_char_skill_rank_data import Act1VHalfIdleCharSkillRankData
from .act1_vhalf_idle_const_data import Act1VHalfIdleConstData
from .act1_vhalf_idle_diagram_data import Act1VHalfIdleDiagramData
from .act1_vhalf_idle_enemy_drop_bundle import Act1VHalfIdleEnemyDropBundle
from .act1_vhalf_idle_equip_data import Act1VHalfIdleEquipData
from .act1_vhalf_idle_gacha_char_data import Act1VHalfIdleGachaCharData
from .act1_vhalf_idle_gacha_pool_data import Act1VHalfIdleGachaPoolData
from .act1_vhalf_idle_gacha_pool_type_data import Act1VHalfIdleGachaPoolTypeData
from .act1_vhalf_idle_milestone_item_data import Act1VHalfIdleMilestoneItemData
from .act1_vhalf_idle_plot_data import Act1VHalfIdlePlotData
from .act1_vhalf_idle_plot_type_data import Act1VHalfIdlePlotTypeData
from .act1_vhalf_idle_stage_production_data import Act1VHalfIdleStageProductionData
from .act1_vhalf_idle_tech_tree_data import Act1VHalfIdleTechTreeData
from .act1_vhalf_idle_trap_meta import Act1VHalfIdleTrapMeta
from .act1_vhalf_idle_weighted_battle_equip import Act1VHalfIdleWeightedBattleEquip
from .act1_vweighted_res_item_bundle import Act1VWeightedResItemBundle


class Act1VHalfIdleData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    gachaPoolData: dict[str, Act1VHalfIdleGachaPoolData]
    gachaCharData: dict[str, Act1VHalfIdleGachaCharData]
    plotTypeData: dict[str, Act1VHalfIdlePlotTypeData]
    plotData: dict[str, Act1VHalfIdlePlotData]
    stageProductionData: dict[str, Act1VHalfIdleStageProductionData]
    charRankData: dict[str, Act1VHalfIdleCharRankData]
    charEvolveData: dict[str, Act1VHalfIdleCharEvolveData]
    charMaxRankData: dict[str, Act1VHalfIdleCharMaxRankData]
    charSkillRankData: dict[str, Act1VHalfIdleCharSkillRankData]
    techTreeData: dict[str, Act1VHalfIdleTechTreeData]
    charBuffData: list[Act1VHalfIdleCharBuffData]
    milestoneList: list[Act1VHalfIdleMilestoneItemData]
    poolTypeData: list[Act1VHalfIdleGachaPoolTypeData]
    stageIds: list[str]
    zoneId: str
    constData: Act1VHalfIdleConstData
    diagramList: list[Act1VHalfIdleDiagramData]
    enemyItemDropPoolDict: dict[str, Act1VHalfIdleEnemyDropBundle]
    battleItemPoolDict: dict[str, list[Act1VBattleItemDropSlot]]
    resourceItemPoolDict: dict[str, list[Act1VWeightedResItemBundle]]
    equipItemPoolDict: dict[str, list[Act1VHalfIdleWeightedBattleEquip]]
    trapItemPoolDict: dict[str, list[str]]
    equipItemData: dict[str, dict[int, list[Act1VHalfIdleEquipData]]]
    trapMetaDict: dict[str, Act1VHalfIdleTrapMeta]
    plotShowCombineHighlightDict: dict[str, list[str]]
