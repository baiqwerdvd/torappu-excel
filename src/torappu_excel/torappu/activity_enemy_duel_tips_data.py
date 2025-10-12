from pydantic import BaseModel, ConfigDict


class ActivityEnemyDuelTipsData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    txt: str
    weight: int
    modeIds: list[str] | None
