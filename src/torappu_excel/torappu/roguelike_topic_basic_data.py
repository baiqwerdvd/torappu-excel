from .roguelike_module_type import RoguelikeModuleType
from .roguelike_topic_config import RoguelikeTopicConfig
from ..common import BaseStruct


class RoguelikeTopicBasicData(BaseStruct):
    id: str
    name: str
    startTime: int
    disappearTimeOnMainScreen: int
    sort: int
    showMedalId: str
    medalGroupId: str
    fullStoredTime: int
    lineText: str
    homeEntryDisplayData: list["RoguelikeTopicBasicData.HomeEntryDisplayData"]
    moduleTypes: list[RoguelikeModuleType]
    config: RoguelikeTopicConfig

    class HomeEntryDisplayData(BaseStruct):
        topicId: str
        displayId: str
        startTs: int
        endTs: int
