from pydantic import BaseModel, ConfigDict


class SandboxFoodStaminaData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    itemId: str
    potCnt: int
    foodStaminaCnt: int
