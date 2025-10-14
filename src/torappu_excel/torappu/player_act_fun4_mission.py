from pydantic import BaseModel, ConfigDict


class PlayerActFun4Mission(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    value: int
    target: int
    finished: bool
    hasRecv: bool
