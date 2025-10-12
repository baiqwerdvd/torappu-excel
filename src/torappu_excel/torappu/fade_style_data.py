from pydantic import BaseModel, ConfigDict


class FadeStyleData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    styleName: str
    fadeinTime: float
    fadeoutTime: float
    fadeinType: str
    fadeoutType: str
