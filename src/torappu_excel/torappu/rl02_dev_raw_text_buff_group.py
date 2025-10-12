from pydantic import BaseModel, ConfigDict


class RL02DevRawTextBuffGroup(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    nodeIdList: list[str]
    useLevelMark: bool
    groupIconId: str
    useUpBreak: bool
    sortId: int
