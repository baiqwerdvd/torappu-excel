from ..common import BaseStruct

from msgspec import field


class FifthAnnivExploreBroadcastData(BaseStruct):
    id_: str = field(name="id")
    eventCount: int
    stageId: str
    content: str
