from pydantic import BaseModel, ConfigDict


class RL03DevRawTextBuffGroup(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    nodeIdList: list[str]
    useLevelMark: bool
    groupIconId: str
    sortId: int
