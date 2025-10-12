from pydantic import BaseModel, ConfigDict

from .roguelike_task_rarity import RoguelikeTaskRarity


class RoguelikeTaskData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    taskId: str
    taskName: str
    taskDesc: str
    rewardSceneId: str
    taskRarity: RoguelikeTaskRarity
