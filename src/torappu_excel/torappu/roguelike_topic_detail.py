from .roguelike_activity_data import RoguelikeActivityData
from .roguelike_archive_component_data import RoguelikeArchiveComponentData
from .roguelike_archive_unlock_cond_data import RoguelikeArchiveUnlockCondData
from .roguelike_band_ref_data import RoguelikeBandRefData
from .roguelike_battle_summery_description_data import RoguelikeBattleSummeryDescriptionData
from .roguelike_difficulty_upgrade_relic_group_data import RoguelikeDifficultyUpgradeRelicGroupData
from .roguelike_ending_detail_text import RoguelikeEndingDetailText
from .roguelike_ending_relic_detail_text import RoguelikeEndingRelicDetailText
from .roguelike_event_type import RoguelikeEventType
from .roguelike_game_char_buff_data import RoguelikeGameCharBuffData
from .roguelike_game_choice_data import RoguelikeGameChoiceData
from .roguelike_game_choice_scene_data import RoguelikeGameChoiceSceneData
from .roguelike_game_const import RoguelikeGameConst
from .roguelike_game_custom_ticket_data import RoguelikeGameCustomTicketData
from .roguelike_game_ending_data import RoguelikeGameEndingData
from .roguelike_game_explore_tool_data import RoguelikeGameExploreToolData
from .roguelike_game_fail_ending_data import RoguelikeGameFailEndingData
from .roguelike_game_init_data import RoguelikeGameInitData
from .roguelike_game_item_data import RoguelikeGameItemData
from .roguelike_game_node_sub_type_data import RoguelikeGameNodeSubTypeData
from .roguelike_game_node_type_data import RoguelikeGameNodeTypeData
from .roguelike_game_recruit_grp_data import RoguelikeGameRecruitGrpData
from .roguelike_game_recruit_ticket_data import RoguelikeGameRecruitTicketData
from .roguelike_game_relic_data import RoguelikeGameRelicData
from .roguelike_game_relic_param_data import RoguelikeGameRelicParamData
from .roguelike_game_shop_dialog_data import RoguelikeGameShopDialogData
from .roguelike_game_shop_dialog_type import RoguelikeGameShopDialogType
from .roguelike_game_squad_buff_data import RoguelikeGameSquadBuffData
from .roguelike_game_stage_data import RoguelikeGameStageData
from .roguelike_game_trap_data import RoguelikeGameTrapData
from .roguelike_game_treasure_data import RoguelikeGameTreasureData
from .roguelike_game_upgrade_ticket_data import RoguelikeGameUpgradeTicketData
from .roguelike_game_variation_data import RoguelikeGameVariationData
from .roguelike_game_zone_data import RoguelikeGameZoneData
from .roguelike_predefined_const_style_data import RoguelikePredefinedConstStyleData
from .roguelike_predefined_style_data import RoguelikePredefinedStyleData
from .roguelike_roll_node_data import RoguelikeRollNodeData
from .roguelike_task_data import RoguelikeTaskData
from .roguelike_topic_bank_reward import RoguelikeTopicBankReward
from .roguelike_topic_bp import RoguelikeTopicBP
from .roguelike_topic_bp_grand_prize import RoguelikeTopicBPGrandPrize
from .roguelike_topic_capsule import RoguelikeTopicCapsule
from .roguelike_topic_challenge import RoguelikeTopicChallenge
from .roguelike_topic_detail_const import RoguelikeTopicDetailConst
from .roguelike_topic_difficulty import RoguelikeTopicDifficulty
from .roguelike_topic_enroll import RoguelikeTopicEnroll
from .roguelike_topic_milestone_update_data import RoguelikeTopicMilestoneUpdateData
from .roguelike_topic_mode import RoguelikeTopicMode
from .roguelike_topic_month_mission import RoguelikeTopicMonthMission
from .roguelike_topic_month_squad import RoguelikeTopicMonthSquad
from .roguelike_topic_update import RoguelikeTopicUpdate
from .roguelike_zone_variation_data import RoguelikeZoneVariationData
from .tip_data import TipData
from ..common import BaseStruct

from msgspec import field


class RoguelikeTopicDetail(BaseStruct):
    updates: list[RoguelikeTopicUpdate]
    enrolls: dict[str, RoguelikeTopicEnroll]
    milestones: list[RoguelikeTopicBP]
    milestoneUpdates: list[RoguelikeTopicMilestoneUpdateData]
    grandPrizes: list[RoguelikeTopicBPGrandPrize]
    monthMission: list[RoguelikeTopicMonthMission]
    monthSquad: dict[str, RoguelikeTopicMonthSquad]
    challenges: dict[str, RoguelikeTopicChallenge]
    difficulties: list[RoguelikeTopicDifficulty]
    bankRewards: list[RoguelikeTopicBankReward]
    archiveComp: RoguelikeArchiveComponentData
    archiveUnlockCond: RoguelikeArchiveUnlockCondData
    detailConst: RoguelikeTopicDetailConst
    init: list[RoguelikeGameInitData]
    stages: dict[str, RoguelikeGameStageData]
    zones: dict[str, RoguelikeGameZoneData]
    variation: dict[str, RoguelikeZoneVariationData]
    traps: dict[str, RoguelikeGameTrapData]
    recruitTickets: dict[str, RoguelikeGameRecruitTicketData]
    upgradeTickets: dict[str, RoguelikeGameUpgradeTicketData]
    customTickets: dict[str, RoguelikeGameCustomTicketData]
    relics: dict[str, RoguelikeGameRelicData]
    relicParams: dict[str, RoguelikeGameRelicParamData]
    recruitGrps: dict[str, RoguelikeGameRecruitGrpData]
    choices: dict[str, RoguelikeGameChoiceData]
    choiceScenes: dict[str, RoguelikeGameChoiceSceneData]
    nodeTypeData: dict[RoguelikeEventType, RoguelikeGameNodeTypeData]
    subTypeData: list[RoguelikeGameNodeSubTypeData]
    variationData: dict[str, RoguelikeGameVariationData]
    charBuffData: dict[str, RoguelikeGameCharBuffData]
    squadBuffData: dict[str, RoguelikeGameSquadBuffData]
    taskData: dict[str, RoguelikeTaskData]
    gameConst: RoguelikeGameConst
    capsuleDict: dict[str, RoguelikeTopicCapsule] | None
    endings: dict[str, RoguelikeGameEndingData]
    failEndings: dict[str, RoguelikeGameFailEndingData]
    battleSummeryDescriptions: dict[RoguelikeTopicMode, RoguelikeBattleSummeryDescriptionData]
    battleLoadingTips: list[TipData]
    items: dict[str, RoguelikeGameItemData]
    bandRef: dict[str, RoguelikeBandRefData]
    endingDetailList: list[RoguelikeEndingDetailText]
    treasures: dict[str, list[RoguelikeGameTreasureData]]
    difficultyUpgradeRelicGroups: dict[str, RoguelikeDifficultyUpgradeRelicGroupData]
    styleConfig: RoguelikePredefinedConstStyleData
    activity: RoguelikeActivityData
    endingRelicDetailList: list[RoguelikeEndingRelicDetailText] | None = field(default=None)
    shopDialogData: RoguelikeGameShopDialogData | None = field(default=None)
    shopDialogs: dict[RoguelikeGameShopDialogType, list[str]] | None = field(default=None)
    styles: dict[str, RoguelikePredefinedStyleData] | None = field(default=None)
    exploreTools: dict[str, RoguelikeGameExploreToolData] | None = field(default=None)
    rollNodeData: dict[str, RoguelikeRollNodeData] | None = field(default=None)
