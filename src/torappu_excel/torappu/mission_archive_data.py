from pydantic import BaseModel, ConfigDict

from .mission_archive_node_data import MissionArchiveNodeData
from .mission_archive_voice_clip_data import MissionArchiveVoiceClipData


class MissionArchiveData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    topicId: str
    zones: list[str]
    nodes: list[MissionArchiveNodeData]
    hiddenClips: list[MissionArchiveVoiceClipData]
    unlockDesc: str
