from .legacy_in_level_rune_data import LegacyInLevelRuneData
from .rune_table import RuneTable
from .sandbox_v2_alchemy_recipe_data import SandboxV2AlchemyRecipeData
from .sandbox_v2_archive_achievement_data import SandboxV2ArchiveAchievementData
from .sandbox_v2_archive_achievement_type_data import SandboxV2ArchiveAchievementTypeData
from .sandbox_v2_archive_music_unlock_data import SandboxV2ArchiveMusicUnlockData
from .sandbox_v2_archive_quest_data import SandboxV2ArchiveQuestData
from .sandbox_v2_archive_quest_type_data import SandboxV2ArchiveQuestTypeData
from .sandbox_v2_base_update_data import SandboxV2BaseUpdateData
from .sandbox_v2_basic_const import SandboxV2BasicConst
from .sandbox_v2_battle_rush_enemy_data import SandboxV2BattleRushEnemyData
from .sandbox_v2_building_item_data import SandboxV2BuildingItemData
from .sandbox_v2_building_node_score_data import SandboxV2BuildingNodeScoreData
from .sandbox_v2_challenge_mode_data import SandboxV2ChallengeModeData
from .sandbox_v2_confirm_icon_data import SandboxV2ConfirmIconData
from .sandbox_v2_craft_group_data import SandboxV2CraftGroupData
from .sandbox_v2_craft_item_data import SandboxV2CraftItemData
from .sandbox_v2_development_const import SandboxV2DevelopmentConst
from .sandbox_v2_development_data import SandboxV2DevelopmentData
from .sandbox_v2_development_line_segment_data import SandboxV2DevelopmentLineSegmentData
from .sandbox_v2_dialog_data import SandboxV2DialogData
from .sandbox_v2_drink_mat_data import SandboxV2DrinkMatData
from .sandbox_v2_enemy_rush_type_data import SandboxV2EnemyRushTypeData
from .sandbox_v2_event_choice_data import SandboxV2EventChoiceData
from .sandbox_v2_event_data import SandboxV2EventData
from .sandbox_v2_event_effect_data import SandboxV2EventEffectData
from .sandbox_v2_event_scene_data import SandboxV2EventSceneData
from .sandbox_v2_expedition_data import SandboxV2ExpeditionData
from .sandbox_v2_fixed_rift_data import SandboxV2FixedRiftData
from .sandbox_v2_float_icon_data import SandboxV2FloatIconData
from .sandbox_v2_food_data import SandboxV2FoodData
from .sandbox_v2_food_mat_data import SandboxV2FoodMatData
from .sandbox_v2_game_const import SandboxV2GameConst
from .sandbox_v2_guide_quest_data import SandboxV2GuideQuestData
from .sandbox_v2_item_trap_data import SandboxV2ItemTrapData
from .sandbox_v2_item_trap_tag_data import SandboxV2ItemTrapTagData
from .sandbox_v2_livestock_data import SandboxV2LivestockData
from .sandbox_v2_logistics_char_data import SandboxV2LogisticsCharData
from .sandbox_v2_logistics_data import SandboxV2LogisticsData
from .sandbox_v2_map_data import SandboxV2MapData
from .sandbox_v2_month_rush_data import SandboxV2MonthRushData
from .sandbox_v2_node_buff_data import SandboxV2NodeBuffData
from .sandbox_v2_node_type_data import SandboxV2NodeTypeData
from .sandbox_v2_node_upgrade_data import SandboxV2NodeUpgradeData
from .sandbox_v2_npc_data import SandboxV2NpcData
from .sandbox_v2_quest_data import SandboxV2QuestData
from .sandbox_v2_quest_line_data import SandboxV2QuestLineData
from .sandbox_v2_racing_data import SandboxV2RacingData
from .sandbox_v2_reward_config_group_data import SandboxV2RewardConfigGroupData
from .sandbox_v2_rift_const import SandboxV2RiftConst
from .sandbox_v2_rift_difficulty_data import SandboxV2RiftDifficultyData
from .sandbox_v2_rift_global_effect_data import SandboxV2RiftGlobalEffectData
from .sandbox_v2_rift_main_target_data import SandboxV2RiftMainTargetData
from .sandbox_v2_rift_param_data import SandboxV2RiftParamData
from .sandbox_v2_rift_sub_target_data import SandboxV2RiftSubTargetData
from .sandbox_v2_rift_team_buff_data import SandboxV2RiftTeamBuffData
from .sandbox_v2_season_data import SandboxV2SeasonData
from .sandbox_v2_shop_dialog_data import SandboxV2ShopDialogData
from .sandbox_v2_shop_good_data import SandboxV2ShopGoodData
from .sandbox_v2_stage_data import SandboxV2StageData
from .sandbox_v2_tutorial_data import SandboxV2TutorialData
from .sandbox_v2_weather_data import SandboxV2WeatherData
from .sandbox_v2_zone_data import SandboxV2ZoneData
from .tip_data import TipData
from ..common import BaseStruct


class SandboxV2Data(BaseStruct):
    mapData: dict[str, SandboxV2MapData]
    itemTrapData: dict[str, SandboxV2ItemTrapData]
    itemTrapTagData: dict[str, SandboxV2ItemTrapTagData]
    buildingItemData: dict[str, SandboxV2BuildingItemData]
    craftItemData: dict[str, SandboxV2CraftItemData]
    livestockProduceData: dict[str, SandboxV2LivestockData]
    craftGroupData: dict[str, SandboxV2CraftGroupData]
    alchemyRecipeData: dict[str, SandboxV2AlchemyRecipeData]
    drinkMatData: dict[str, SandboxV2DrinkMatData]
    foodMatData: dict[str, SandboxV2FoodMatData]
    foodData: dict[str, SandboxV2FoodData]
    nodeTypeData: dict[str, SandboxV2NodeTypeData]
    nodeUpgradeData: dict[str, SandboxV2NodeUpgradeData]
    weatherData: dict[str, SandboxV2WeatherData]
    stageData: dict[str, SandboxV2StageData]
    zoneData: dict[str, SandboxV2ZoneData]
    nodeBuffData: dict[str, SandboxV2NodeBuffData]
    rewardConfigData: SandboxV2RewardConfigGroupData
    floatIconData: dict[str, SandboxV2FloatIconData]
    enemyRushTypeData: dict[str, SandboxV2EnemyRushTypeData]
    rushEnemyData: SandboxV2BattleRushEnemyData
    gameConst: SandboxV2GameConst
    basicConst: SandboxV2BasicConst
    riftConst: SandboxV2RiftConst
    developmentConst: SandboxV2DevelopmentConst
    battleLoadingTips: list[TipData]
    runeDatas: dict[str, RuneTable.PackedRuneData]
    itemRuneList: dict[str, list[LegacyInLevelRuneData]]
    questData: dict[str, SandboxV2QuestData]
    npcData: dict[str, SandboxV2NpcData]
    dialogData: dict[str, SandboxV2DialogData]
    questLineData: dict[str, SandboxV2QuestLineData]
    questLineStoryData: dict[str, str]
    guideQuestData: dict[str, SandboxV2GuideQuestData]
    developmentData: dict[str, SandboxV2DevelopmentData]
    eventData: dict[str, SandboxV2EventData]
    eventSceneData: dict[str, SandboxV2EventSceneData]
    eventChoiceData: dict[str, SandboxV2EventChoiceData]
    expeditionData: dict[str, SandboxV2ExpeditionData]
    eventEffectData: dict[str, SandboxV2EventEffectData]
    shopGoodData: dict[str, SandboxV2ShopGoodData]
    shopDialogData: SandboxV2ShopDialogData
    logisticsData: list[SandboxV2LogisticsData]
    logisticsCharMapping: dict[str, dict[str, list[SandboxV2LogisticsCharData]]]
    materialKeywordData: dict[str, str]
    monthRushData: list[SandboxV2MonthRushData]
    riftTerrainParamData: dict[str, SandboxV2RiftParamData]
    riftClimateParamData: dict[str, SandboxV2RiftParamData]
    riftEnemyParamData: dict[str, SandboxV2RiftParamData]
    riftSubTargetData: dict[str, SandboxV2RiftSubTargetData]
    riftMainTargetData: dict[str, SandboxV2RiftMainTargetData]
    riftGlobalEffectData: dict[str, SandboxV2RiftGlobalEffectData]
    fixedRiftData: dict[str, SandboxV2FixedRiftData]
    riftTeamBuffData: dict[str, list[SandboxV2RiftTeamBuffData]]
    riftDifficultyData: dict[str, SandboxV2RiftDifficultyData]
    riftRewardDisplayData: dict[str, list[str]]
    enemyReplaceData: dict[str, dict[str, str]]
    archiveQuestData: dict[str, SandboxV2ArchiveQuestData]
    achievementData: dict[str, SandboxV2ArchiveAchievementData]
    achievementTypeData: dict[str, SandboxV2ArchiveAchievementTypeData]
    archiveQuestTypeData: dict[str, SandboxV2ArchiveQuestTypeData]
    archiveMusicUnlockData: dict[str, SandboxV2ArchiveMusicUnlockData]
    baseUpdate: list[SandboxV2BaseUpdateData]
    developmentLineSegmentDatas: list[SandboxV2DevelopmentLineSegmentData]
    buildingNodeScoreData: dict[str, SandboxV2BuildingNodeScoreData]
    seasonData: dict[str, SandboxV2SeasonData]
    confirmIconData: list[SandboxV2ConfirmIconData]
    shopUpdateTimeData: list[int]
    tutorialData: SandboxV2TutorialData
    racingData: SandboxV2RacingData
    challengeModeData: SandboxV2ChallengeModeData
