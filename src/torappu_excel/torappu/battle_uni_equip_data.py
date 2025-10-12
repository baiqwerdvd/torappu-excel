from pydantic import BaseModel, ConfigDict

from .character_data import CharacterData
from .uni_equip_target import UniEquipTarget


class BattleUniEquipData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    resKey: str | None
    target: "UniEquipTarget"
    isToken: bool
    validInGameTag: str | None
    validInMapTag: str | None
    addOrOverrideTalentDataBundle: "CharacterData.EquipTalentDataBundle"
    overrideTraitDataBundle: "CharacterData.EquipTraitDataBundle"
