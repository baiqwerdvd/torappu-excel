from pydantic import BaseModel, ConfigDict

from .uni_equip_type import UniEquipType


class UniEquipTrack(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    charId: str
    equipId: str
    type: UniEquipType
    archiveShowTimeEnd: int
