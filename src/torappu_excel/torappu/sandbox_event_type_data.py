from .sandbox_event_type import SandboxEventType
from ..common import BaseStruct


class SandboxEventTypeData(BaseStruct):
    eventType: SandboxEventType
    iconId: str
