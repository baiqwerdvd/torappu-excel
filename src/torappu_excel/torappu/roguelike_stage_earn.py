from pydantic import BaseModel, ConfigDict


class RoguelikeStageEarn(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    exp: int
    populationMax: int
    squadCapacity: int
    hp: int
    shield: int
    maxHpUp: int
