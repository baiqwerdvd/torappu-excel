from .roguelike_task_rarity import RoguelikeTaskRarity
from ..common import BaseStruct


class RoguelikeTaskData(BaseStruct):
    taskId: str
    taskName: str
    taskDesc: str
    rewardSceneId: str
    taskRarity: RoguelikeTaskRarity
