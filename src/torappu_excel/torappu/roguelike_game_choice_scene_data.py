from ..common import BaseStruct


class RoguelikeGameChoiceSceneData(BaseStruct):
    id: str
    title: str
    description: str
    background: str | None
    titleIcon: str | None
    subTypeId: int
    useHiddenMusic: bool
