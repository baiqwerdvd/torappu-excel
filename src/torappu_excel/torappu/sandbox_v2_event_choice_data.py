from .sandbox_v2_event_choice_type import SandboxV2EventChoiceType
from ..common import BaseStruct

from msgspec import field


class SandboxV2EventChoiceData(BaseStruct):
    choiceId: str
    type_: SandboxV2EventChoiceType = field(name="type")
    costAction: int
    title: str
    desc: str
    expeditionId: str | None
