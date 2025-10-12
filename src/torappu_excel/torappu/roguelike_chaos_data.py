from pydantic import BaseModel, ConfigDict


class RoguelikeChaosData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    chaosId: str
    level: int
    nextChaosId: str | None
    prevChaosId: str | None
    iconId: str
    name: str
    functionDesc: str
    desc: str
    sound: str
    sortId: int
