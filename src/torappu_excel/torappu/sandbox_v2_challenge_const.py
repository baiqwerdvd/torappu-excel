from pydantic import BaseModel, ConfigDict


class SandboxV2ChallengeConst(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    challengeModeDesc: str
    dailyTitleDesc: str
    debuffCountdownDesc: str
    gainAllDebuffDesc: str
    dailyUpAttributeDesc: str
