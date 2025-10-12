from pydantic import BaseModel, ConfigDict

from .voice_lang_type import VoiceLangType


class VoiceLangGroupData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    name: str
    members: list[VoiceLangType]
