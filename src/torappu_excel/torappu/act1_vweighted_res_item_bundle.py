from pydantic import BaseModel, ConfigDict


class Act1VWeightedResItemBundle(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    weight: float
    resources: dict[str, int]
