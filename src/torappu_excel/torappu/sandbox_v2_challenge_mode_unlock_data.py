from pydantic import BaseModel, ConfigDict


class SandboxV2ChallengeModeUnlockData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    unlockId: str
    sortId: int
    conditionDesc: str
