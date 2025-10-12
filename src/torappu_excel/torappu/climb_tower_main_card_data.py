from pydantic import BaseModel, ConfigDict

from .climb_tower_card_type import ClimbTowerCardType
from .rune_table import RuneTable


class ClimbTowerMainCardData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    type: ClimbTowerCardType
    linkedTowerId: str | None
    sortId: int
    name: str
    desc: str
    subCardIds: list[str]
    runeData: RuneTable.PackedRuneData | None
    trapIds: list[str]
