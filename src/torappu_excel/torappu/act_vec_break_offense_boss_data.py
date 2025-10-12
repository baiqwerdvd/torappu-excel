from pydantic import BaseModel, ConfigDict


class ActVecBreakOffenseBossData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    enemyId: str
    name: str
    desc: str
    level: int
    iconId: str
