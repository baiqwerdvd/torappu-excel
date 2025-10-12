from pydantic import BaseModel, ConfigDict

from .sandbox_event_type import SandboxEventType


class SandboxEventSceneData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    choiceSceneId: str
    type: SandboxEventType
    title: str
    description: str
    choices: list[str]
