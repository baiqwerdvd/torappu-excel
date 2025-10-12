from pydantic import BaseModel, ConfigDict

from .roguelike_buff import RoguelikeBuff


class RoguelikeGameSquadBuffData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    iconId: str
    outerName: str
    innerName: str
    functionDesc: str
    desc: str
    buffs: list[RoguelikeBuff]
