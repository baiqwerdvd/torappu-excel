from ..common import BaseStruct

from msgspec import field


class RoguelikeGameChoiceSceneData(BaseStruct):
    id_: str = field(name="id")
    title: str
    description: str
    background: str | None
    titleIcon: str | None
    subTypeId: int
    useHiddenMusic: bool
