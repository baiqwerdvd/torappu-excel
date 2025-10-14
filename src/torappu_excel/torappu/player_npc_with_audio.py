from pydantic import BaseModel, ConfigDict

from .voice_lang_type import VoiceLangType


class PlayerNpcWithAudio(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    npcShowAudioInfoFlag: VoiceLangType
