from ..common import BaseStruct

from msgspec import field


class RoguelikeChoiceSceneData(BaseStruct):
    id_: str = field(name="id")
    title: str
    description: str
    background: str
