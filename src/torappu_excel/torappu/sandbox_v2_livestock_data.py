from pydantic import BaseModel, ConfigDict


class SandboxV2LivestockData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    livestockItemId: str
    shinyLivestockItemId: str
    livestockEnemyId: str
    targetFenceId: str
