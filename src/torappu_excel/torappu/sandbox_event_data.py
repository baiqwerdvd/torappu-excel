from pydantic import BaseModel, ConfigDict


class SandboxEventData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    eventSceneId: str
    hasThumbtack: bool
