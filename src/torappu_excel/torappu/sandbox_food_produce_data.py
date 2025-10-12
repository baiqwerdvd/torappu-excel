from pydantic import BaseModel, ConfigDict


class SandboxFoodProduceData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    itemId: str
    mainMaterialItems: list[str]
    buffId: str
    unlockDesc: str
