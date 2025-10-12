from pydantic import BaseModel, ConfigDict


class SandboxV2BaseUpdateCondition(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    desc: str
    limitCond: str
    param: list[str]
