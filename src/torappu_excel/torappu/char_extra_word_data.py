from msgspec import field

from ..common import BaseStruct


class CharExtraWordData(BaseStruct):
    wordKey: str
    charId: str
    voiceId: str
    voiceText: str
    charWordId: str | None = field(default=None)
