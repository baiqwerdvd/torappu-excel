from pydantic import BaseModel, ConfigDict


class Act42SideTrustorData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    trustorId: str
    sortId: int
    trustorName: str
    trustorIconSmall: str
    trustorIconLarge: str
    gunId: str
    taskList: list[str]
