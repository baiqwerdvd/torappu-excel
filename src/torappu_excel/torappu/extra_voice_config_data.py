from pydantic import BaseModel, ConfigDict

from .voice_lang_type import VoiceLangType


class ExtraVoiceConfigData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    voiceId: str
    validVoiceLang: list[VoiceLangType]
