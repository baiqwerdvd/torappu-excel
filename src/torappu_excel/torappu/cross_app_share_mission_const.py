from pydantic import BaseModel, ConfigDict, Field


class CrossAppShareMissionConst(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    nameCardShareMissionId: str = Field(default="")
