from pydantic import BaseModel, ConfigDict


class ActMultiV3TipsData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    txt: str
    weight: int
