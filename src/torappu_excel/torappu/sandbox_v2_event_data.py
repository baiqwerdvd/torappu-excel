from pydantic import BaseModel, ConfigDict

from .sandbox_v2_event_type import SandboxV2EventType


class SandboxV2EventData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    eventId: str
    type: SandboxV2EventType
    iconId: str
    iconName: str | None
    enterSceneId: str
