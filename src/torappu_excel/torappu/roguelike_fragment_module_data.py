from .alchemy_pool_rarity_type import AlchemyPoolRarityType
from .roguelike_event_type import RoguelikeEventType
from .roguelike_fragment_type import RoguelikeFragmentType
from .roguelike_game_item_type import RoguelikeGameItemType
from ..common import BaseStruct

from msgspec import field


class RoguelikeFragmentModuleData(BaseStruct):
    class RoguelikeFragmentData(BaseStruct):
        id_: str = field(name="id")
        type_: RoguelikeFragmentType = field(name="type")
        value: int
        weight: int

    class RoguelikeFragmentTypeData(BaseStruct):
        type_: RoguelikeFragmentType = field(name="type")
        typeName: str
        typeDesc: str
        typeIconId: str

    class RoguelikeFragmentModuleConsts(BaseStruct):
        weightStatusSafeDesc: str
        weightStatusLimitDesc: str
        weightStatusOverweightDesc: str
        charWeightSlot: int
        limitWeightThresholdValue: int
        overWeightThresholdValue: int
        maxAlchemyField: int
        maxAlchemyCount: int
        fragmentBagWeightLimitTips: str
        fragmentBagWeightOverWeightTips: str
        weightUpgradeToastFormat: str

    class RoguelikeFragmentBuffData(BaseStruct):
        itemId: str
        maskType: RoguelikeEventType
        desc: str | None

    class RoguelikeAlchemyData(BaseStruct):
        fragmentTypeList: list[RoguelikeFragmentType]
        fragmentSquareSum: int
        poolRarity: AlchemyPoolRarityType
        relicProp: float
        shieldProp: float
        populationProp: float
        overrideConditionBandIds: list[str] | None
        overrideRecipeId: str | None

    class RoguelikeAlchemyFormulationData(BaseStruct):
        fragmentIds: list[str]
        rewardId: str
        rewardCount: int
        rewardItemType: RoguelikeGameItemType

    class RoguelikeFragmentLevelRelatedData(BaseStruct):
        weightUp: int

    fragmentData: dict[str, "RoguelikeFragmentModuleData.RoguelikeFragmentData"]
    fragmentTypeData: dict[str, "RoguelikeFragmentModuleData.RoguelikeFragmentTypeData"]
    moduleConsts: "RoguelikeFragmentModuleData.RoguelikeFragmentModuleConsts"
    fragmentBuffData: dict[str, "RoguelikeFragmentModuleData.RoguelikeFragmentBuffData"]
    alchemyData: dict[str, "RoguelikeFragmentModuleData.RoguelikeAlchemyData"]
    alchemyFormulaData: dict[str, "RoguelikeFragmentModuleData.RoguelikeAlchemyFormulationData"]
    fragmentLevelData: dict[str, "RoguelikeFragmentModuleData.RoguelikeFragmentLevelRelatedData"]
