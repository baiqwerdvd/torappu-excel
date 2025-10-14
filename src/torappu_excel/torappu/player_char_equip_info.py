from pydantic import BaseModel, ConfigDict


class PlayerCharEquipInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    hide: int
    locked: bool
    level: int
