from pydantic import BaseModel, ConfigDict


class CrisisV2AppraiseWrap(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    appraiseType: str
