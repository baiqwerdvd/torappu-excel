from .act1_vhalf_idle_equip_type import Act1VHalfIdleEquipType
from .rune_table import RuneTable
from ..common import BaseStruct


class Act1VHalfIdleEquipData(BaseStruct):
    equipId: str
    alias: str
    iconId: str
    name: str
    level: int
    equipType: Act1VHalfIdleEquipType
    runeData: "RuneTable.PackedRuneData"
