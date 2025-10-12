from pydantic import BaseModel, ConfigDict


class ActMultiV3TargetMissionData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    sortId: int
    title: str
    battleDesc: str
    description: str
