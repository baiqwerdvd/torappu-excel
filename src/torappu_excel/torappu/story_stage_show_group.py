from .stage_diff_group import StageDiffGroup
from ..common import BaseStruct


class StoryStageShowGroup(BaseStruct):
    displayRecordId: str
    stageId: str
    accordingStageId: str | None
    diffGroup: StageDiffGroup
