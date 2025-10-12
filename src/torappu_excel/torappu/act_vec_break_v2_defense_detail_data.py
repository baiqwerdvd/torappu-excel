from pydantic import BaseModel, ConfigDict


class ActVecBreakV2DefenseDetailData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    stageId: str
    buffId: str
    defenseCharLimit: int
    bossIconId: str
