from pydantic import BaseModel, ConfigDict


class PlayerGoodProgressData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    count: int
    order: int
