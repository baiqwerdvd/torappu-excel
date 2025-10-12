from pydantic import Field

from .roguelike_buff import RoguelikeBuff


class RoguelikeOuterBuff(RoguelikeBuff):
    level: int
    name: str
    iconId: str
    description: str
    usage: str
    buffId: str | None = Field(default=None)
