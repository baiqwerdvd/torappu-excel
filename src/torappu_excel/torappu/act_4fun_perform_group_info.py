from pydantic import BaseModel, ConfigDict


class Act4funPerformGroupInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    performGroupId: str
    performIds: list[str]
