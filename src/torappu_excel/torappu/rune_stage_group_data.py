from pydantic import BaseModel, ConfigDict


class RuneStageGroupData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    groupId: str
    activeRuneStages: list["RuneStageGroupData.RuneStageInst"]
    startTs: int
    endTs: int

    class RuneStageInst(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        stageId: str
        activePackedRuneIds: list[str]
