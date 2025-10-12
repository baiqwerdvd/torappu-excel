from pydantic import BaseModel, ConfigDict

from .voice_lang_group_type import VoiceLangGroupType


class VoiceLangTypeData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    name: str
    groupType: VoiceLangGroupType
