from pydantic import BaseModel, ConfigDict


class SandboxV2GuideQuestData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    questId: str
    storyId: str
    triggerKey: str
