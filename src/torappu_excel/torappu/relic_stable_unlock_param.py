from pydantic import BaseModel, ConfigDict


class RelicStableUnlockParam(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    unlockCondDetail: str
    unlockCnt: int
