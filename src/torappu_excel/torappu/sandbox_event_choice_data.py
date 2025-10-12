from pydantic import BaseModel, ConfigDict

from .sandbox_event_choice_type import SandboxEventChoiceType


class SandboxEventChoiceData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    choiceId: str
    type: SandboxEventChoiceType
    costAction: int
    finishScene: bool
    title: str
    description: str
