from pydantic import BaseModel, ConfigDict


class SandboxStageData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    stageId: str
    levelId: str
    code: str
    name: str
    loadingPicId: str
    description: str
    actionCost: int
    powerCost: int
