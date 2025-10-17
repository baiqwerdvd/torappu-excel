from .mission_archive_node_data import MissionArchiveNodeData
from .mission_archive_voice_clip_data import MissionArchiveVoiceClipData
from ..common import BaseStruct


class MissionArchiveData(BaseStruct):
    topicId: str
    zones: list[str]
    nodes: list[MissionArchiveNodeData]
    hiddenClips: list[MissionArchiveVoiceClipData]
    unlockDesc: str
