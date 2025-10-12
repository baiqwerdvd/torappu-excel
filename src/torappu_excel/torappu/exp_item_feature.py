from pydantic import BaseModel, ConfigDict


class ExpItemFeature(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    gainExp: int
