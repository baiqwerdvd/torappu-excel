from pydantic import BaseModel, ConfigDict


class RoguelikeTotemSubBuffData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    subBuffId: str
    name: str
    desc: str
    combinedDesc: str
    info: str
