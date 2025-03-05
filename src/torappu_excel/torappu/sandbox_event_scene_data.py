from .sandbox_event_type import SandboxEventType
from ..common import BaseStruct

from msgspec import field


class SandboxEventSceneData(BaseStruct):
    choiceSceneId: str
    type_: SandboxEventType = field(name="type")
    title: str
    description: str
    choices: list[str]
