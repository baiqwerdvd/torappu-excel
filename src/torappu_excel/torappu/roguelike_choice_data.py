from ..common import BaseStruct


class RoguelikeChoiceData(BaseStruct):
    id: str
    title: str
    description: str | None
    type: str
    nextSceneId: str | None
    icon: str | None
    param: dict[str, object]
