from pydantic import BaseModel, ConfigDict, Field

from torappu_excel.common import CustomIntEnum

from .attributes_data import AttributesData
from .blackboard import Blackboard
from .buildable_type import BuildableTypeStr
from .equip_talent_data import EquipTalentData
from .evolve_phase import EvolvePhase
from .external_buff import ExternalBuff
from .item_bundle import ItemBundle
from .profession_category import ProfessionCategory
from .rarity_rank import RarityRank
from .shared_models import CharacterData as SharedCharacterData
from .special_operator_target_type import SpecialOperatorTargetType
from .talent_data import TalentData


class CharacterData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    name: str
    description: str | None
    spTargetType: SpecialOperatorTargetType
    spTargetId: str | None
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
    sortIndex: int | None = Field(default=None)
    mainPower: "PowerData | None" = Field(default=None)
    subPower: list["PowerData"] | None = Field(default=None)
    minPowerId: str | None = Field(default=None)
    maxPowerId: str | None = Field(default=None)
    displayTokenDict: dict[str, bool] | None = Field(default=None)
    classicPotentialItemId: str | None = Field(default=None)
    tokenKey: str | None = Field(default=None)

    class SkillLevelCost(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        unlockCond: "SharedCharacterData.UnlockCondition"
        lvlUpCost: list[ItemBundle] | None

    class PotentialRank(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        class TypeEnum(CustomIntEnum):
            BUFF = "BUFF", 0
            CUSTOM = "CUSTOM", 1

        type: TypeEnum
        description: str
        buff: ExternalBuff | None
        equivalentCost: list[ItemBundle] | None

    class AttributesDeltaKeyFrame(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        pass

    class UnlockCondition(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        phase: EvolvePhase
        level: int

    class TalentDataBundle(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        candidates: list[TalentData] | None

    class MasterData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        level: int
        masterId: str
        talentData: TalentData

    class MainSkill(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        skillId: str | None
        overridePrefabKey: str | None
        overrideTokenKey: str | None
        levelUpCostCond: list["CharacterData.MainSkill.SpecializeLevelData"]
        unlockCond: "SharedCharacterData.UnlockCondition"

        class SpecializeLevelData(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            unlockCond: "SharedCharacterData.UnlockCondition"
            lvlUpTime: int
            levelUpCost: list[ItemBundle] | None

    class AttributesKeyFrame(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        level: int
        data: AttributesData

    class PhaseData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        characterPrefabKey: str
        rangeId: str | None
        maxLevel: int
        attributesKeyFrames: list["CharacterData.AttributesKeyFrame"]
        evolveCost: list[ItemBundle] | None

    class TraitData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        unlockCondition: "SharedCharacterData.UnlockCondition"
        requiredPotentialRank: int
        blackboard: list[Blackboard]
        overrideDescripton: str | None
        prefabKey: str | None
        rangeId: str | None
        additionalDesc: str | None = Field(default=None)

    class TraitDataBundle(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        candidates: list["CharacterData.TraitData"]

    class EquipTalentDataBundle(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        candidates: list["EquipTalentData"] | None

    class EquipTraitData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        additionalDescription: str | None
        unlockCondition: "SharedCharacterData.UnlockCondition"
        requiredPotentialRank: int
        blackboard: list[Blackboard]
        overrideDescripton: str | None
        prefabKey: str | None
        rangeId: str | None

    class EquipTraitDataBundle(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        candidates: list["CharacterData.EquipTraitData"] | None

    class PowerData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        nationId: str | None
        groupId: str | None
        teamId: str | None


class TokenCharacterData(CharacterData):
    skills: list["CharacterData.MainSkill"] | None  # pyright: ignore[reportIncompatibleVariableOverride]
    potentialRanks: list["CharacterData.PotentialRank"] | None  # pyright: ignore[reportIncompatibleVariableOverride]
    allSkillLvlup: list["CharacterData.SkillLevelCost"] | None  # pyright: ignore[reportIncompatibleVariableOverride]


class MasterDataBundle(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    candidates: list["CharacterData.MasterData"] | None
