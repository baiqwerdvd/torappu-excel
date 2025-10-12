from pydantic import BaseModel, ConfigDict


class SandboxV2EventEffectData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    eventEffectId: str
    buffId: str
    duration: int
    desc: str
