from pydantic import BaseModel, ConfigDict


class EnemyHandbookRaceData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    raceName: str
    sortId: int
