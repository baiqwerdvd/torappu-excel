from pydantic import BaseModel, ConfigDict


class OpenServerChainLogin(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    isAvailable: bool
    nowIndex: int
    history: list[bool]
