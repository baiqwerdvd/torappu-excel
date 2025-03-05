from ..common import BaseStruct

from msgspec import field


class FifthAnnivExploreEventChoiceData(BaseStruct):
    id_: str = field(name="id")
    eventId: str
    name: str
    desc: str
    successDesc: str
    failureDesc: str
