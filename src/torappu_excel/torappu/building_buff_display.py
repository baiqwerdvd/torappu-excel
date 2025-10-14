from pydantic import BaseModel, ConfigDict


class BuildingBuffDisplay(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    base: int
    buff: int
