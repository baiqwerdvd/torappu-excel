from .roguelike_buff import RoguelikeBuff

from msgspec import field


class RoguelikeOuterBuff(RoguelikeBuff):
    level: int
    name: str
    iconId: str
    description: str
    usage: str
    buffId: str | None = field(default=None)
