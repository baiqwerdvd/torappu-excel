from pydantic import BaseModel, ConfigDict


class SandboxBuildProduceUnlockData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    itemId: str
    buildingEffectDesc: str
    buildingItemDesc: str
    buildingUnlockDesc: str
