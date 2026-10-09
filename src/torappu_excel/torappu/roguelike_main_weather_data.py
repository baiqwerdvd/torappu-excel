from ..common import BaseStruct


class RoguelikeMainWeatherData(BaseStruct):
    id: str
    iconId: str
    iconBigId: str
    isPositive: bool
    level: int
    name: str
    levelName: str
    type: str
    functionDesc: str
    desc: str
    sound: str | None
