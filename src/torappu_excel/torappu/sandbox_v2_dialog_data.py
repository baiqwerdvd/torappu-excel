from pydantic import BaseModel, ConfigDict


class SandboxV2DialogData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    dialogId: str
    avgId: str
