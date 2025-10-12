from pydantic import BaseModel, ConfigDict


class ActVecBreakV2DefenseGroupData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    groupId: str | None
    sortId: int
    orderedStageList: list[str]
