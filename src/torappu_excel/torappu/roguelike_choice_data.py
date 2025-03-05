from ..common import BaseStruct

from msgspec import field


class RoguelikeChoiceData(BaseStruct):
    id_: str = field(name="id")
    title: str
    description: str | None
    type_: str = field(name="type")
    nextSceneId: str | None
    icon: str | None
    param: dict[str, object]
