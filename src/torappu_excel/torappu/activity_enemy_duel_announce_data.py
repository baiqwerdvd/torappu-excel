from pydantic import BaseModel, ConfigDict


class ActivityEnemyDuelAnnounceData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    startTs: int
    endTs: int
    announceText: str
    showNew: bool
