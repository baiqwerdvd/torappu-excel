from pydantic import BaseModel, ConfigDict


class GuideMissionGroupInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    groupId: str
    sortId: int
    shortName: str
    unlockDesc: str | None
