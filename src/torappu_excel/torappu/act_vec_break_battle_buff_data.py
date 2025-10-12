from pydantic import BaseModel, ConfigDict

from .rune_table import RuneTable


class ActVecBreakBattleBuffData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    buffId: str
    openTime: int
    name: str
    desc: str
    iconId: str
    runeData: "RuneTable.PackedRuneData"
