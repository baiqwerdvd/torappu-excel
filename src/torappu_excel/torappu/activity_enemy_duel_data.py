from pydantic import BaseModel, ConfigDict

from .activity_enemy_duel_announce_data import ActivityEnemyDuelAnnounceData
from .activity_enemy_duel_const_data import ActivityEnemyDuelConstData
from .activity_enemy_duel_const_toast_data import ActivityEnemyDuelConstToastData
from .activity_enemy_duel_enemy_data import ActivityEnemyDuelEnemyData
from .activity_enemy_duel_extra_score_group_data import ActivityEnemyDuelExtraScoreGroupData
from .activity_enemy_duel_milestone_item_data import ActivityEnemyDuelMilestoneItemData
from .activity_enemy_duel_mode_data import ActivityEnemyDuelModeData
from .activity_enemy_duel_npc_data import ActivityEnemyDuelNpcData
from .activity_enemy_duel_npc_selector_group_data import ActivityEnemyDuelNpcSelectorGroupData
from .activity_enemy_duel_pool_data import ActivityEnemyDuelPoolData
from .activity_enemy_duel_round_data import ActivityEnemyDuelRoundData
from .activity_enemy_duel_single_comment_data import ActivityEnemyDuelSingleCommentData
from .activity_enemy_duel_tips_data import ActivityEnemyDuelTipsData


class ActivityEnemyDuelData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    milestoneList: list[ActivityEnemyDuelMilestoneItemData]
    modeData: dict[str, ActivityEnemyDuelModeData]
    roundData: dict[str, ActivityEnemyDuelRoundData]
    poolData: dict[str, ActivityEnemyDuelPoolData]
    npcData: dict[str, ActivityEnemyDuelNpcData]
    npcSelectorData: dict[str, ActivityEnemyDuelNpcSelectorGroupData]
    enemyData: dict[str, ActivityEnemyDuelEnemyData]
    extraScoreData: dict[str, ActivityEnemyDuelExtraScoreGroupData]
    basicScores: list[int]
    announceData: list[ActivityEnemyDuelAnnounceData]
    commentData: dict[str, dict[str, ActivityEnemyDuelSingleCommentData]]
    constData: ActivityEnemyDuelConstData
    constToastData: ActivityEnemyDuelConstToastData
    tipsData: list[ActivityEnemyDuelTipsData]
    enabledEmoticonThemeIdList: list[str]
