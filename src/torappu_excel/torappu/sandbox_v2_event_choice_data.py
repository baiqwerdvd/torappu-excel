from .sandbox_v2_event_choice_type import SandboxV2EventChoiceType
from ..common import BaseStruct


class SandboxV2EventChoiceData(BaseStruct):
    choiceId: str
    type: SandboxV2EventChoiceType
    costAction: int
    title: str
    desc: str
    expeditionId: str | None
