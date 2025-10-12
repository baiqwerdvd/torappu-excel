from pydantic import BaseModel, ConfigDict, Field

from .blackboard import Blackboard
from .shared_models import CharacterData as SharedCharacterData


class TalentData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    unlockCondition: "SharedCharacterData.UnlockCondition"
    requiredPotentialRank: int
    prefabKey: str
    name: str | None
    description: str | None
    rangeId: str | None
    blackboard: list[Blackboard]
    displayRange: bool = False
    tokenKey: str | None = Field(default=None)
    isHideTalent: bool = False
