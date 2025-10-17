from .act_5fun_basic_const import Act5funBasicConst
from .act_5fun_basic_npc_data import Act5FunBasicNpcData
from .act_5fun_choice_reward_data import Act5FunChoiceRewardData
from .act_5fun_const import Act5funConst
from .act_5fun_enemy_id_mapping_data import Act5FunEnemyIdMappingData
from .act_5fun_npc_data import Act5FunNpcData
from .act_5fun_npc_selector_data import Act5FunNpcSelectorData
from .act_5fun_round_data import Act5FunRoundData
from .act_5fun_settle_rating_data import Act5FunSettleRatingData
from .act_5fun_settle_streak_data import Act5FunSettleStreakData
from .act_5fun_settle_success_data import Act5FunSettleSuccessData
from ..common import BaseStruct


class Act5FunData(BaseStruct):
    battleData: "Act5FunData.BattleData"
    constData: Act5funBasicConst
    npcData: dict[str, Act5FunBasicNpcData]
    ratingData: list[Act5FunSettleRatingData]
    streakData: list[Act5FunSettleStreakData]
    successData: list[Act5FunSettleSuccessData]

    class BattleData(BaseStruct):
        battleConstData: Act5funConst
        roundData: dict[str, Act5FunRoundData]
        npcData: dict[str, Act5FunNpcData]
        npcSelectorData: list[Act5FunNpcSelectorData]
        choiceRewardData: dict[str, Act5FunChoiceRewardData]
        enemyIdMappingData: dict[str, Act5FunEnemyIdMappingData]
        battleStreak: list[float]
