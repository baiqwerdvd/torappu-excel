from .activity_enemy_duel_extra_score_data import ActivityEnemyDuelExtraScoreData
from ..common import BaseStruct


class ActivityEnemyDuelExtraScoreGroupData(BaseStruct):
    modeId: str
    data: list[ActivityEnemyDuelExtraScoreData]
