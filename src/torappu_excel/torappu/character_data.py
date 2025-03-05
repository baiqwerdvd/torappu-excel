# pyright: reportIncompatibleVariableOverride=false
from .attributes_data import AttributesData
from .blackboard import Blackboard
from .buildable_type import BuildableTypeStr
from .equip_talent_data import EquipTalentData
from .external_buff import ExternalBuff
from .item_bundle import ItemBundle
from .profession_category import ProfessionCategory
from .rarity_rank import RarityRank
from .shared_models import CharacterData as SharedCharacterData
from .talent_data import TalentData
from ..common import BaseStruct, CustomIntEnum

from msgspec import field


class CharacterData(BaseStruct):
    name: str
    description: str | None
    canUseGeneralPotentialItem: bool
    canUseActivityPotentialItem: bool
    potentialItemId: str | None
    activityPotentialItemId: str | None
    nationId: str | None
    groupId: str | None
    teamId: str | None
    displayNumber: str | None
    appellation: str
    position: BuildableTypeStr
    tagList: list[str] | None
    itemUsage: str | None
    itemDesc: str | None
    itemObtainApproach: str | None
    isNotObtainable: bool
    isSpChar: bool
    maxPotentialLevel: int
    rarity: RarityRank
    profession: ProfessionCategory
    subProfessionId: str
    trait: "CharacterData.TraitDataBundle | None"
    phases: list["CharacterData.PhaseData"]
    skills: list["CharacterData.MainSkill"]
    talents: list["CharacterData.TalentDataBundle"] | None
    potentialRanks: list["CharacterData.PotentialRank"]
    favorKeyFrames: list["CharacterData.AttributesKeyFrame"] | None
    allSkillLvlup: list["CharacterData.SkillLevelCost"]
    minPowerId: str | None = field(default=None)
    maxPowerId: str | None = field(default=None)
    displayTokenDict: dict[str, bool] | None = field(default=None)
    classicPotentialItemId: str | None = field(default=None)
    tokenKey: str | None = field(default=None)

    class SkillLevelCost(BaseStruct):
        unlockCond: "SharedCharacterData.UnlockCondition"
        lvlUpCost: list[ItemBundle] | None

    class PotentialRank(BaseStruct):
        class TypeEnum(CustomIntEnum):
            BUFF = "BUFF", 0
            CUSTOM = "CUSTOM", 1

        type_: TypeEnum = field(name="type")
        description: str
        buff: ExternalBuff | None
        equivalentCost: list[ItemBundle] | None

    class TalentDataBundle(BaseStruct):
        candidates: list[TalentData] | None

    class MainSkill(BaseStruct):
        skillId: str | None
        overridePrefabKey: str | None
        overrideTokenKey: str | None
        levelUpCostCond: list["CharacterData.MainSkill.SpecializeLevelData"]
        unlockCond: "SharedCharacterData.UnlockCondition"

        class SpecializeLevelData(BaseStruct):
            unlockCond: "SharedCharacterData.UnlockCondition"
            lvlUpTime: int
            levelUpCost: list[ItemBundle] | None

    class AttributesKeyFrame(BaseStruct):
        level: int
        data: AttributesData

    class PhaseData(BaseStruct):
        characterPrefabKey: str
        rangeId: str | None
        maxLevel: int
        attributesKeyFrames: list["CharacterData.AttributesKeyFrame"]
        evolveCost: list[ItemBundle] | None

    class TraitData(BaseStruct):
        unlockCondition: "SharedCharacterData.UnlockCondition"
        requiredPotentialRank: int
        blackboard: list[Blackboard]
        overrideDescripton: str | None
        prefabKey: str | None
        rangeId: str | None
        additionalDesc: str | None = field(default=None)

    class TraitDataBundle(BaseStruct):
        candidates: list["CharacterData.TraitData"]

    class EquipTalentDataBundle(BaseStruct):
        candidates: list["EquipTalentData"] | None

    class EquipTraitData(BaseStruct):
        additionalDescription: str | None
        unlockCondition: "SharedCharacterData.UnlockCondition"
        requiredPotentialRank: int
        blackboard: list[Blackboard]
        overrideDescripton: str | None
        prefabKey: str | None
        rangeId: str | None

    class EquipTraitDataBundle(BaseStruct):
        candidates: list["CharacterData.EquipTraitData"] | None


class TokenCharacterData(CharacterData):
    skills: list["CharacterData.MainSkill"] | None
    potentialRanks: list["CharacterData.PotentialRank"] | None
    allSkillLvlup: list["CharacterData.SkillLevelCost"] | None
