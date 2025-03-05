from ..common import BaseStruct


class NewVoiceTimeData(BaseStruct):
    timestamp: int
    charSet: list[str]
