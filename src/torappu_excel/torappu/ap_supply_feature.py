from pydantic import BaseModel, ConfigDict


class ApSupplyFeature(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    ap: int
    hasTs: bool
