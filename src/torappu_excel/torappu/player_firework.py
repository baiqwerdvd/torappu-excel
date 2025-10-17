from .firework_data import FireworkData
from ..common import BaseStruct


class PlayerFirework(BaseStruct):
    unlock: bool
    plate: "PlayerFirework.PlayerPlate"
    animal: "PlayerFirework.PlayerAnimal"

    class PlayerPlate(BaseStruct):
        unlock: dict[str, int]
        slots: "list[FireworkData.PlateSlotData]"

    class PlayerAnimal(BaseStruct):
        unlock: dict[str, int]
        select: str
