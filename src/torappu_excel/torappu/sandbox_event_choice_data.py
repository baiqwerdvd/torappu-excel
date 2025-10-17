from .sandbox_event_choice_type import SandboxEventChoiceType
from ..common import BaseStruct


class SandboxEventChoiceData(BaseStruct):
    choiceId: str
    type: SandboxEventChoiceType
    costAction: int
    finishScene: bool
    title: str
    description: str
