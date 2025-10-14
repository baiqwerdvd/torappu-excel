from enum import IntEnum, StrEnum

from pydantic import BaseModel, ConfigDict


class SharedConsts(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    class Direction(IntEnum):
        UP = 0
        RIGHT = 1
        DOWN = 2
        LEFT = 3
        E_NUM = 4
        INVALID = 4

    class DirectionStr(StrEnum):
        UP = "UP"
        RIGHT = "RIGHT"
        DOWN = "DOWN"
        LEFT = "LEFT"
        E_NUM = "E_NUM"
        INVALID = "INVALID"
