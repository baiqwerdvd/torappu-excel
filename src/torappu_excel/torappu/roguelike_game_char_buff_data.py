from pydantic import BaseModel, ConfigDict

from .roguelike_buff import RoguelikeBuff
from .roguelike_game_char_buff_type import RoguelikeGameCharBuffType


class RoguelikeGameCharBuffData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    buffType: RoguelikeGameCharBuffType
    iconId: str
    outerName: str
    innerName: str
    functionDesc: str
    desc: str
    buffs: list[RoguelikeBuff]
