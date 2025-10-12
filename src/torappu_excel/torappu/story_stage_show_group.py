from pydantic import BaseModel, ConfigDict

from .stage_diff_group import StageDiffGroup


class StoryStageShowGroup(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    displayRecordId: str
    stageId: str
    accordingStageId: str | None
    diffGroup: StageDiffGroup
