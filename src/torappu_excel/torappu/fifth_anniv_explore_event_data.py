from ..common import BaseStruct


class FifthAnnivExploreEventData(BaseStruct):
    id: str
    name: str
    typeName: str
    iconId: str
    desc: str
    choiceIds: list[str]
