from pydantic import BaseModel, ConfigDict, Field

from .blackboard import Blackboard
from .shared_models import CharacterData as SharedCharacterData


class EquipTalentData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    displayRangeId: bool
    upgradeDescription: str
    talentIndex: int
    unlockCondition: "SharedCharacterData.UnlockCondition"
    requiredPotentialRank: int
    prefabKey: str
    name: str | None
    description: str | None
    rangeId: str | None
    blackboard: list["Blackboard"]
    tokenKey: str | None = Field(default=None)
    isHideTalent: bool | None = Field(default=None)
