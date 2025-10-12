from pydantic import BaseModel, ConfigDict


class ActVecBreakV2DefenseBasicData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    stageId: str
    groupId: str | None
    sortId: int
    startTs: int
