from pydantic import BaseModel, ConfigDict


class Act1VHalfIdleWeightedBattleEquip(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    weight: float
    equipId: str
    level: int
    alias: str
