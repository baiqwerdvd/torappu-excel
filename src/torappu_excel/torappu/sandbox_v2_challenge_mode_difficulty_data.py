from pydantic import BaseModel, ConfigDict


class SandboxV2ChallengeModeDifficultyData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    challengeDay: int
    diffDesc: str
