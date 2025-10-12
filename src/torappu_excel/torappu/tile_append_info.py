from pydantic import BaseModel, ConfigDict


class TileAppendInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    tileKey: str
    name: str
    description: str
    isFunctional: bool
