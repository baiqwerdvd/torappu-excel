from .san_effect_rank import SanEffectRank
from ..common import BaseStruct


class RoguelikeSanRangeData(BaseStruct):
    sanMax: int
    diceGroupId: str
    description: str
    sanDungeonEffect: SanEffectRank
    sanEffectRank: SanEffectRank
    sanEndingDesc: str | None
