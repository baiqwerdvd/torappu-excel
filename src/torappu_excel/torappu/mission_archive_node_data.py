from .mission_archive_voice_clip_data import MissionArchiveVoiceClipData
from ..common import BaseStruct


class MissionArchiveNodeData(BaseStruct):
    nodeId: str
    title: str
    unlockDesc: str
    clips: list[MissionArchiveVoiceClipData]
