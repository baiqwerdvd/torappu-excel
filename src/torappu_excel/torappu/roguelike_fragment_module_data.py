from pydantic import BaseModel, ConfigDict

from .alchemy_pool_rarity_type import AlchemyPoolRarityType
from .roguelike_event_type import RoguelikeEventType
from .roguelike_fragment_type import RoguelikeFragmentType
from .roguelike_game_item_type import RoguelikeGameItemType


class RoguelikeFragmentModuleData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    fragmentData: dict[str, "RoguelikeFragmentModuleData.RoguelikeFragmentData"]
    fragmentTypeData: dict[str, "RoguelikeFragmentModuleData.RoguelikeFragmentTypeData"]
    moduleConsts: "RoguelikeFragmentModuleData.RoguelikeFragmentModuleConsts"
    fragmentBuffData: dict[str, "RoguelikeFragmentModuleData.RoguelikeFragmentBuffData"]
    alchemyData: dict[str, "RoguelikeFragmentModuleData.RoguelikeAlchemyData"]
    alchemyFormulaData: dict[str, "RoguelikeFragmentModuleData.RoguelikeAlchemyFormulationData"]
    fragmentLevelData: dict[str, "RoguelikeFragmentModuleData.RoguelikeFragmentLevelRelatedData"]

    class RoguelikeFragmentData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        id: str
        type: RoguelikeFragmentType
        value: int
        weight: int

    class RoguelikeFragmentTypeData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        type: RoguelikeFragmentType
        typeName: str
        typeDesc: str
        typeIconId: str

    class RoguelikeFragmentModuleConsts(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

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

    class RoguelikeFragmentBuffData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        itemId: str
        maskType: RoguelikeEventType
        desc: str | None

    class RoguelikeAlchemyData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        fragmentTypeList: list[RoguelikeFragmentType]
        fragmentSquareSum: int
        poolRarity: AlchemyPoolRarityType
        relicProp: float
        shieldProp: float
        populationProp: float
        overrideConditionBandIds: list[str] | None
        overrideRecipeId: str | None

    class RoguelikeAlchemyFormulationData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        fragmentIds: list[str]
        rewardId: str
        rewardCount: int
        rewardItemType: RoguelikeGameItemType

    class RoguelikeFragmentLevelRelatedData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        weightUp: int
