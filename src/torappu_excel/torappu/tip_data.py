from enum import StrEnum

from pydantic import BaseModel, ConfigDict


class TipData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    class Category(StrEnum):
        NONE = "NONE"
        BATTLE = "BATTLE"
        UI = "UI"
        BUILDING = "BUILDING"
        GACHA = "GACHA"
        MISC = "MISC"
        ALL = "ALL"

    tip: str
    weight: float | int
    category: "TipData.Category"
