from pydantic import BaseModel, ConfigDict


class PlayerActFun5(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    stageState: dict[str, int]
    highScore: int
