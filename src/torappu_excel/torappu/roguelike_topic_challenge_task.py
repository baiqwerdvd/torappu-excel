from ..common import BaseStruct


class RoguelikeTopicChallengeTask(BaseStruct):
    taskId: str
    taskDes: str
    completionClass: str
    completionParams: list[str]
