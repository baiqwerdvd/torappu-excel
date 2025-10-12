from pydantic import BaseModel, ConfigDict


class ActivityEnemyDuelExtraScoreData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    rankMin: int
    rankMax: int
    tokenNum: int
