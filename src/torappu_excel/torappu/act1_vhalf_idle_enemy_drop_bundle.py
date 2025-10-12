from pydantic import BaseModel, ConfigDict


class Act1VHalfIdleEnemyDropBundle(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    exp: int
    mileStoneCnt: int
    battleItemDropPool: str
    resourceItemDropPool: str
