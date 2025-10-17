from .item_bundle import ItemBundle
from ..common import BaseStruct


class Act42SideTaskData(BaseStruct):
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
