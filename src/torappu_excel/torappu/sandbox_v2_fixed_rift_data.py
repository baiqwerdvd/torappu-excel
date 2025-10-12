from pydantic import BaseModel, ConfigDict


class SandboxV2FixedRiftData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    riftId: str
    riftName: str
    rewardGroupId: str
