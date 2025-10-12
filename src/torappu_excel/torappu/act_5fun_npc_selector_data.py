from pydantic import BaseModel, ConfigDict


class Act5FunNpcSelectorData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    npcId: str
    enemyId: str
    score: float
