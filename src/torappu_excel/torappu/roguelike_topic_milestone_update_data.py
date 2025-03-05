from ..common import BaseStruct


class RoguelikeTopicMilestoneUpdateData(BaseStruct):
    updateTime: int
    endTime: int
    maxBpLevel: int
    maxBpCount: int
    maxDisplayBpCount: int
