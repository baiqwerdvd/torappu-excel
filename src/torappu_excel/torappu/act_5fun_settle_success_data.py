from pydantic import BaseModel, ConfigDict


class Act5FunSettleSuccessData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    count: int
    desc: str
