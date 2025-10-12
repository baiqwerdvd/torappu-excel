from pydantic import BaseModel, ConfigDict

from .rune_table import RuneTable


class RecalRuneRuneData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    runeId: str
    score: int
    sortId: int
    essential: bool
    exclusiveGroupId: str | None
    runeIcon: str | None
    packedRune: "RuneTable.PackedRuneData"
