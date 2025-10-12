from pydantic import BaseModel, ConfigDict

from .sandbox_event_type import SandboxEventType


class SandboxEventTypeData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    eventType: SandboxEventType
    iconId: str
