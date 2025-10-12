from pydantic import BaseModel, ConfigDict

from .data_unlock_type import DataUnlockType


class HandbookUnlockParam(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    unlockType: DataUnlockType
    unlockParam1: str
    unlockParam2: str | None
    unlockParam3: str | None
