from pydantic import BaseModel, ConfigDict


class RoguelikeWrathData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    group: str
    level: int
    name: str
    levelName: str
    functionDesc: str
    desc: str
