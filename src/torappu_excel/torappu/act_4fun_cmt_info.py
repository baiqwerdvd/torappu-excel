from pydantic import BaseModel, ConfigDict


class Act4funCmtInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    iconId: str | None
    name: str | None
    cmtTxt: str
