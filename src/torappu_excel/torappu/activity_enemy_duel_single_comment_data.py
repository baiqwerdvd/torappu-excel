from pydantic import BaseModel, ConfigDict


class ActivityEnemyDuelSingleCommentData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    commentId: str
    priority: int
    template: str
    param: list[str]
    commentText: str
