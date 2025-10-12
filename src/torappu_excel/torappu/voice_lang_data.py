from pydantic import BaseModel, ConfigDict, Field

from .voice_lang_info_data import VoiceLangInfoData
from .voice_lang_type import VoiceLangType


class VoiceLangData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    wordkeys: list[str]
    charId: str
    dict_: dict[VoiceLangType, VoiceLangInfoData] = Field(alias="dict")
