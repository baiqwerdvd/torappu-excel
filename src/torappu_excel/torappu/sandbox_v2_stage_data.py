from pydantic import BaseModel, ConfigDict


class SandboxV2StageData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    stageId: str
    levelId: str
    code: str
    name: str
    description: str
    actionCost: int
    actionCostEnemyRush: int
