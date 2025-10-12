from pydantic import BaseModel, ConfigDict


class RoguelikeModeData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    name: str
    canUnlockItem: int
    scoreFactor: float
    itemPools: list[str]
    difficultyDesc: str
    ruleDesc: str
    sortId: int
    unlockMode: str
    color: str
