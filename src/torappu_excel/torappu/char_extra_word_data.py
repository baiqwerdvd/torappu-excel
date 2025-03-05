from ..common import BaseStruct

from msgspec import field


class CharExtraWordData(BaseStruct):
    wordKey: str
    charId: str
    voiceId: str
    voiceText: str
    charWordId: str | None = field(default=None)
