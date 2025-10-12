from pydantic import BaseModel, ConfigDict


class SoundFXCtrlBank(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    name: str
    targetBank: str
    ctrlStop: bool
    ctrlStopFadetime: float
