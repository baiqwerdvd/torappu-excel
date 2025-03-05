from .character_data import CharacterData
from .uni_equip_target import UniEquipTarget
from ..common import BaseStruct


class BattleUniEquipData(BaseStruct):
    resKey: str | None
    target: "UniEquipTarget"
    isToken: bool
    validInGameTag: str | None
    addOrOverrideTalentDataBundle: "CharacterData.EquipTalentDataBundle"
    overrideTraitDataBundle: "CharacterData.EquipTraitDataBundle"
