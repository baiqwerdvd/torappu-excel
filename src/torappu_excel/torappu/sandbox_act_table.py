from .legacy_in_level_rune_data import LegacyInLevelRuneData
from .rune_table import RuneTable
from .rush_enemy_group import RushEnemyGroup
from .sandbox_base_const_table import SandboxBaseConstTable
from .sandbox_build_gold_ratio_data import SandboxBuildGoldRatioData
from .sandbox_build_produce_data import SandboxBuildProduceData
from .sandbox_build_produce_unlock_data import SandboxBuildProduceUnlockData
from .sandbox_building_item_data import SandboxBuildingItemData
from .sandbox_craft_item_data import SandboxCraftItemData
from .sandbox_daily_desc_template_data import SandboxDailyDescTemplateData
from .sandbox_daily_desc_template_type import SandboxDailyDescTemplateType
from .sandbox_development_data import SandboxDevelopmentData
from .sandbox_development_limit_data import SandboxDevelopmentLimitData
from .sandbox_development_line_segment_data import SandboxDevelopmentLineSegmentData
from .sandbox_event_choice_data import SandboxEventChoiceData
from .sandbox_event_data import SandboxEventData
from .sandbox_event_scene_data import SandboxEventSceneData
from .sandbox_event_type import SandboxEventType
from .sandbox_event_type_data import SandboxEventTypeData
from .sandbox_food_produce_data import SandboxFoodProduceData
from .sandbox_food_stamina_data import SandboxFoodStaminaData
from .sandbox_foodmat_buff_data import SandboxFoodmatBuffData
from .sandbox_item_toast_data import SandboxItemToastData
from .sandbox_item_trap_data import SandboxItemTrapData
from .sandbox_item_type import SandboxItemType
from .sandbox_map_const_table import SandboxMapConstTable
from .sandbox_mission_data import SandboxMissionData
from .sandbox_node_type import SandboxNodeType
from .sandbox_node_type_data import SandboxNodeTypeData
from .sandbox_node_upgrade_data import SandboxNodeUpgradeData
from .sandbox_reward_config_group_data import SandboxRewardConfigGroupData
from .sandbox_stage_data import SandboxStageData
from .sandbox_stamina_data import SandboxStaminaData
from .sandbox_unit_data import SandboxUnitData
from .sandbox_weather_data import SandboxWeatherData
from .tip_data import TipData
from ..common import BaseStruct


class SandboxActTable(BaseStruct):
    mapConstTable: SandboxMapConstTable
    baseConstTable: SandboxBaseConstTable
    battleLoadingTips: list[TipData]
    foodProduceDatas: dict[str, SandboxFoodProduceData]
    foodmatDatas: dict[str, SandboxFoodmatBuffData]
    foodmatBuffDatas: dict[str, SandboxFoodmatBuffData]
    foodStaminaDatas: dict[str, SandboxFoodStaminaData]
    buildProduceDatas: dict[str, SandboxBuildProduceData]
    buildGoldRatioDatas: list[SandboxBuildGoldRatioData]
    buildingItemDatas: dict[str, SandboxBuildingItemData]
    buildProduceUnlockDatas: dict[str, SandboxBuildProduceUnlockData]
    craftItemDatas: dict[str, SandboxCraftItemData]
    itemTrapDatas: dict[str, SandboxItemTrapData]
    trapDeployLimitDatas: dict[str, int]
    developmentDatas: dict[str, SandboxDevelopmentData]
    developmentLimitDatas: dict[str, SandboxDevelopmentLimitData]
    itemToastDatas: dict[SandboxItemType, SandboxItemToastData]
    developmentLineSegmentDatas: list[SandboxDevelopmentLineSegmentData]
    rewardConfigDatas: SandboxRewardConfigGroupData
    charStaminaMapping: dict[str, dict[str, list[SandboxStaminaData]]]
    nodeTypeDatas: dict[SandboxNodeType, SandboxNodeTypeData]
    nodeUpgradeDatas: dict[str, SandboxNodeUpgradeData]
    weatherDatas: dict[str, SandboxWeatherData]
    stageDatas: dict[str, SandboxStageData]
    eventDatas: dict[str, SandboxEventData]
    eventSceneDatas: dict[str, SandboxEventSceneData]
    eventChoiceDatas: dict[str, SandboxEventChoiceData]
    eventTypeDatas: dict[SandboxEventType, SandboxEventTypeData]
    missionDatas: dict[str, SandboxMissionData]
    unitData: dict[str, SandboxUnitData]
    dailyDescTemplateDatas: dict[SandboxDailyDescTemplateType, SandboxDailyDescTemplateData]
    rushAvgDict: dict[str, str]
    rushEnemyGroup: RushEnemyGroup
    runeDatas: dict[str, RuneTable.PackedRuneData]
    itemRuneList: dict[str, list[LegacyInLevelRuneData]]
