from .rune_data import RuneData
from ..common import BaseStruct


class RuneTable(BaseStruct):
    runeStages: list["RuneTable.RuneStageExtraData"]

    class PackedRuneData(BaseStruct):
        id: str
        points: float
        mutexGroupKey: str | None
        description: str | None
        runes: list[RuneData]

    class RuneStageExtraData(BaseStruct):
        stageId: str
        runes: list["RuneTable.PackedRuneData"]
