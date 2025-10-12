from pydantic import BaseModel, ConfigDict


class SOCharMissionGroup(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    groupId: str
    missionIds: list[str]
    startTs: int
    endTs: int
