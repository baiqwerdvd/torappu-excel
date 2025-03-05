from .sandbox_v2_event_type import SandboxV2EventType
from ..common import BaseStruct

from msgspec import field


class SandboxV2EventData(BaseStruct):
    eventId: str
    type_: SandboxV2EventType = field(name="type")
    iconId: str
    iconName: str | None
    enterSceneId: str
