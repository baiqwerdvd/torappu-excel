from ..common import BaseStruct


class RoguelikeSubWeatherData(BaseStruct):
    id: str
    iconId: str
    isPositive: bool
    name: str
    type: str
    functionDesc: str
    desc: str
    sound: str | None
