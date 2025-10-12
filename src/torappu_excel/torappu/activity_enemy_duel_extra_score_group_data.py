from pydantic import BaseModel, ConfigDict

from .activity_enemy_duel_extra_score_data import ActivityEnemyDuelExtraScoreData


class ActivityEnemyDuelExtraScoreGroupData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    modeId: str
    data: list[ActivityEnemyDuelExtraScoreData]
