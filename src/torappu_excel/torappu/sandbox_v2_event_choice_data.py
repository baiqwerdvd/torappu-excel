from pydantic import BaseModel, ConfigDict

from .sandbox_v2_event_choice_type import SandboxV2EventChoiceType


class SandboxV2EventChoiceData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    choiceId: str
    type: SandboxV2EventChoiceType
    costAction: int
    title: str
    desc: str
    expeditionId: str | None
