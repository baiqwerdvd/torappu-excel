from pydantic import BaseModel, ConfigDict

from .npc_strategy import NpcStrategy


class Act5FunNpcData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    npcId: str
    avatarId: str
    name: str
    priority: float | int
    specialStrategy: NpcStrategy
    npcProb: float | int
    defaultEnemyScore: float | int
