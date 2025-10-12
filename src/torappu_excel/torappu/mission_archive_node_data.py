from pydantic import BaseModel, ConfigDict

from .mission_archive_voice_clip_data import MissionArchiveVoiceClipData


class MissionArchiveNodeData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    nodeId: str
    title: str
    unlockDesc: str
    clips: list[MissionArchiveVoiceClipData]
