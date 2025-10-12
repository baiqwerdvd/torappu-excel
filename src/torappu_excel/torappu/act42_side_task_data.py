from pydantic import BaseModel, ConfigDict

from .item_bundle import ItemBundle


class Act42SideTaskData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    taskId: str
    preposedTaskId: str | None
    trustorId: str
    trustorName: str
    sortId: int
    taskName: str
    taskContent: str
    afterTaskContent: str
    beforeTaskItemIcon: str
    afterTaskItemIcon: str
    stageId: str
    taskDesc: str
    rewards: list[ItemBundle]
