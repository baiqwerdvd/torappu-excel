from pydantic import BaseModel, ConfigDict


class Act5FunEnemyIdMappingData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    enemyId: str
    originalEnemyId: str
