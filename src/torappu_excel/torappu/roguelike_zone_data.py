from ..common import BaseStruct

from msgspec import field


class RoguelikeZoneData(BaseStruct):
    id_: str = field(name="id")
    name: str
    description: str
    endingDescription: str
    backgroundId: str
    subIconId: str
