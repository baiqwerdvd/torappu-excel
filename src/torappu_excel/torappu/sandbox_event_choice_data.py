from .sandbox_event_choice_type import SandboxEventChoiceType
from ..common import BaseStruct

from msgspec import field


class SandboxEventChoiceData(BaseStruct):
    choiceId: str
    type_: SandboxEventChoiceType = field(name="type")
    costAction: int
    finishScene: bool
    title: str
    description: str
