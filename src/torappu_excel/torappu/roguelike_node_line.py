from enum import StrEnum

from pydantic import BaseModel, ConfigDict


class RoguelikeNodeLine(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    x: int
    y: int
    hidden: "RoguelikeNodeLine.HiddenType"
    key: bool

    class HiddenType(StrEnum):
        SHOW = "SHOW"
        HIDE = "HIDE"
        APPEAR = "APPEAR"
