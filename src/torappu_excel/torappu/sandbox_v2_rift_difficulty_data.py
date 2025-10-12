from pydantic import BaseModel, ConfigDict


class SandboxV2RiftDifficultyData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    riftId: str
    desc: str
    difficultyLevel: int
    rewardGroupId: str
