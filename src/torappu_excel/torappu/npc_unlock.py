from pydantic import BaseModel, ConfigDict, Field

from .data_unlock_type import DataUnlockType


class NPCUnlock(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    unLockType: DataUnlockType
    unLockParam: str
    unLockString: str | None = Field(default=None)
