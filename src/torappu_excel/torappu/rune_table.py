from .rune_data import RuneData
from ..common import BaseStruct

from msgspec import field


class RuneTable(BaseStruct):
    runeStages: list["RuneTable.RuneStageExtraData"]

    class PackedRuneData(BaseStruct):
        id_: str = field(name="id")
        points: float
        mutexGroupKey: str | None
        description: str | None
        runes: list[RuneData]

    class RuneStageExtraData(BaseStruct):
        stageId: str
        runes: list["RuneTable.PackedRuneData"]
