from .sandbox_event_type import SandboxEventType
from ..common import BaseStruct


class SandboxEventSceneData(BaseStruct):
    choiceSceneId: str
    type: SandboxEventType
    title: str
    description: str
    choices: list[str]
