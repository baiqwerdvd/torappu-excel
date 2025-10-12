from pydantic import BaseModel, ConfigDict


class RoguelikeDiceData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    diceId: str
    description: str
    isUpgradeDice: int
    upgradeDiceId: str | None
    diceFaceCount: int
    battleDiceId: str
