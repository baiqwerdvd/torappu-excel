from pydantic import BaseModel, ConfigDict


class PlayerBuildingFurnitureInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    count: int
    inUse: int
