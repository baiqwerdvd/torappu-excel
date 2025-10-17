from .sandbox_v2_event_type import SandboxV2EventType
from ..common import BaseStruct


class SandboxV2EventData(BaseStruct):
    eventId: str
    type: SandboxV2EventType
    iconId: str
    iconName: str | None
    enterSceneId: str
