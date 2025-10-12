from pydantic import BaseModel, ConfigDict

from .roguelike_module_type import RoguelikeModuleType
from .roguelike_topic_config import RoguelikeTopicConfig


class RoguelikeTopicBasicData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

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

    class HomeEntryDisplayData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        topicId: str
        displayId: str
        startTs: int
        endTs: int
