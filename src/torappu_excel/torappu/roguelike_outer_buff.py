from msgspec import field

from .roguelike_buff import RoguelikeBuff


class RoguelikeOuterBuff(RoguelikeBuff):
    level: int
    name: str
    iconId: str
    description: str
    usage: str
    buffId: str | None = field(default=None)
