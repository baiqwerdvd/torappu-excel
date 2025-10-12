from pydantic import BaseModel, ConfigDict

from .activity_enemy_duel_npc_selector_data import ActivityEnemyDuelNpcSelectorData


class ActivityEnemyDuelNpcSelectorGroupData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    npcId: str
    data: list[ActivityEnemyDuelNpcSelectorData]
