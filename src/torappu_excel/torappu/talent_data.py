from .blackboard import Blackboard
from .shared_models import CharacterData as SharedCharacterData
from ..common import BaseStruct

from msgspec import field


class TalentData(BaseStruct):
    unlockCondition: "SharedCharacterData.UnlockCondition"
    requiredPotentialRank: int
    prefabKey: str
    name: str | None
    description: str | None
    rangeId: str | None
    blackboard: list[Blackboard]
    displayRange: bool = False
    tokenKey: str | None = field(default=None)
    isHideTalent: bool = False
