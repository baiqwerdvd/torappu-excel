from pydantic import BaseModel, ConfigDict


class SandboxV2RiftParamData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    desc: str
    iconId: str
    bkColor: str
