from pydantic import BaseModel, ConfigDict


class PlayerSocialReward(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    canReceive: bool
    first: int
    assistAmount: int
    comfortAmount: int
