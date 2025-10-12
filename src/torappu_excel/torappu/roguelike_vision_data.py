from pydantic import BaseModel, ConfigDict


class RoguelikeVisionData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    sightNum: int
    level: int
    canForesee: bool
    dividedDis: int
    status: str
    clr: str
    desc1: str
    desc2: str
    icon: str
