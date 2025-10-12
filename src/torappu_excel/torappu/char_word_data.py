from pydantic import BaseModel, ConfigDict, Field

from .char_word_show_type import CharWordShowType
from .char_word_unlock_param import CharWordUnlockParam
from .char_word_voice_type import CharWordVoiceType
from .data_unlock_type import DataUnlockType


class CharWordData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    wordKey: str
    charId: str
    voiceId: str
    voiceText: str
    voiceTitle: str
    voiceIndex: int
    voiceType: CharWordVoiceType
    unlockType: DataUnlockType
    unlockParam: list[CharWordUnlockParam]
    lockDescription: str | None
    placeType: CharWordShowType
    voiceAsset: str
    charWordId: str | None = Field(default=None)
