from pydantic import BaseModel, ConfigDict


class MissionArchiveVoiceClipData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    charId: str
    voiceId: str
    index: int
