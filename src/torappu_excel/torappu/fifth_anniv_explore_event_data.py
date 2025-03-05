from ..common import BaseStruct

from msgspec import field


class FifthAnnivExploreEventData(BaseStruct):
    id_: str = field(name="id")
    name: str
    typeName: str
    iconId: str
    desc: str
    choiceIds: list[str]
