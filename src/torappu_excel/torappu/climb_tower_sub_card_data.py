from pydantic import BaseModel, ConfigDict

from .rune_table import RuneTable


class ClimbTowerSubCardData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    mainCardId: str
    sortId: int
    name: str
    desc: str
    runeData: RuneTable.PackedRuneData | None
    trapIds: list[str]
