from pydantic import BaseModel, ConfigDict

from .rune_table import RuneTable


class Act1VHalfIdleCharBuffInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    level: int
    charCount: int
    desc: str
    runeData: "RuneTable.PackedRuneData"
