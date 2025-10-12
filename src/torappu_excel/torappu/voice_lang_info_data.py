from pydantic import BaseModel, ConfigDict, Field

from .voice_lang_type import VoiceLangType


class VoiceLangInfoData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    wordkey: str
    voiceLangType: VoiceLangType
    cvName: list[str]
    voicePath: str | None = Field(default=None)
