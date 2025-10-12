from pydantic import BaseModel, ConfigDict


class SandboxV2ArchiveQuestAvgData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    avgId: str
    avgName: str
