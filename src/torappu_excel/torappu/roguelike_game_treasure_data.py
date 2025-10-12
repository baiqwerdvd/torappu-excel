from pydantic import BaseModel, ConfigDict


class RoguelikeGameTreasureData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    treasureId: str
    groupId: str
    subIndex: int
    name: str
    usage: str
