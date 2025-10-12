from pydantic import BaseModel, ConfigDict


class SandboxV2ArchiveQuestCgData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    cgId: str
    cgTitle: str
    cgDesc: str
    cgPath: str
