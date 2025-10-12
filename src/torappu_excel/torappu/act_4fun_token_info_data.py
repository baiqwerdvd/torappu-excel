from pydantic import BaseModel, ConfigDict


class Act4funTokenInfoData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    tokenLevelId: str
    levelDesc: str | None
    skillDesc: str
    tokenLevelNum: int
    levelIconId: str
