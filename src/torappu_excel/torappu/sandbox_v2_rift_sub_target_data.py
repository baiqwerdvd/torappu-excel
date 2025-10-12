from pydantic import BaseModel, ConfigDict


class SandboxV2RiftSubTargetData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    name: str
    desc: str
