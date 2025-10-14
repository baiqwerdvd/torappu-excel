from pydantic import BaseModel, ConfigDict

from .firework_data import FireworkData


class PlayerFirework(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    unlock: bool
    plate: "PlayerFirework.PlayerPlate"
    animal: "PlayerFirework.PlayerAnimal"

    class PlayerPlate(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        unlock: dict[str, int]
        slots: "list[FireworkData.PlateSlotData]"

    class PlayerAnimal(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        unlock: dict[str, int]
        select: str
