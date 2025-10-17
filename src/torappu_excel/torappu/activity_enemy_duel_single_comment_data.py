from ..common import BaseStruct


class ActivityEnemyDuelSingleCommentData(BaseStruct):
    commentId: str
    priority: int
    template: str
    param: list[str]
    commentText: str
