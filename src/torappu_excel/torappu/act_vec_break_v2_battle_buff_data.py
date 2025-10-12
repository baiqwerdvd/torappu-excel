from pydantic import BaseModel, ConfigDict

from .rune_table import RuneTable


class ActVecBreakV2BattleBuffData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    buffId: str
    name: str
    desc: str
    iconId: str
    runeData: "RuneTable.PackedRuneData"
