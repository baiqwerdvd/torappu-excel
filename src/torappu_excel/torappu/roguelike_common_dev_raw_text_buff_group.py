from pydantic import BaseModel, ConfigDict


class RoguelikeCommonDevRawTextBuffGroup(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    nodeIdList: list[str]
    groupIconId: str
    sortId: int
