from pydantic import BaseModel, ConfigDict

from .act1_vhalf_idle_equip_type import Act1VHalfIdleEquipType
from .rune_table import RuneTable


class Act1VHalfIdleEquipData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    equipId: str
    alias: str
    iconId: str
    name: str
    level: int
    equipType: Act1VHalfIdleEquipType
    runeData: "RuneTable.PackedRuneData"
