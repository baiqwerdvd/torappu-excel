from pydantic import BaseModel, ConfigDict


class PlayerEquipMission(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    value: int
    target: int
