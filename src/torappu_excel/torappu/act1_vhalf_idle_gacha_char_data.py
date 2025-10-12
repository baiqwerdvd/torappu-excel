from pydantic import BaseModel, ConfigDict


class Act1VHalfIdleGachaCharData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    charId: str
    isLinkageChar: bool
